import bokeh.models as bmodels
import bokeh.plotting as plt
import bokeh.palettes as bpalettes
import bokeh.transform as btransform
import bokeh.io
import pandas as pd
import bokeh.layouts as blay
import bokeh.models.widgets as bmw

import server.model.connection as smc
import server.model.event as sme


class Viewer:

    def __init__(self, fname=None, event=None, season=None):
        if event is not None:
            sme.EventDal.set_current_event(event, season)
        conn = smc.pool.getconn()
        sql = "SELECT * FROM vw_measures"
        self.measures = pd.read_sql(sql, conn)

        evt = sme.EventDal.get_current_event()
        evt_id = evt[0]

        sql = """
        SELECT * FROM schedules
        WHERE event_id=%s
        ORDER BY match, alliance;
        """
        self.schedule = pd.read_sql(sql, conn, params=[str(evt_id)])

        sql = """
        SELECT * FROM teams
        WHERE teams.name IN (SELECT team FROM schedules WHERE event_id = %s);
        """
        self.teams = pd.read_sql(sql, conn, params=[str(evt_id)])

    def callback_6t(self, attr, old, new):
        # self.cds_b.data = self.df_new_6t("blue", new)
    #         # df_r = self.df_new_6t("red", new)
    #         # self.cds_r.data = df_r
        print('In callback for match:', new)
        self.layout_6t.children[1] = self.total_6t(new)


    def df_new_6t(self, alliance, match):
        df_teams = self.schedule[(self.schedule.match == match)]
        teams_list = df_teams[(df_teams.alliance == alliance)].team.unique()
        sorted_team = self.measures[self.measures.team.isin(teams_list)]
        sorted_task = sorted_team[sorted_team.task.isin(['shootUpper', 'shootLower'])]
        grouped = sorted_task.groupby(['task', 'team'])
        grouped = grouped.sum()
        grouped = grouped.drop(columns=grouped.columns[1:5])
        df_unstacked = grouped.unstack()
        df_unstacked.columns = df_unstacked.columns.droplevel()
        df_fil = df_unstacked.fillna(0)
        df_fil.loc['Total PC', :] = list(df_fil.sum())
        print(df_fil)
        return df_fil

    def total_6t(self, match):
        self.cds_r = bmodels.ColumnDataSource(self.df_new_6t("red", match))
        all_teams = list(pd.unique(self.schedule.team.sort_values()))
        num_teams = len(all_teams)
        self.cds_b = bmodels.ColumnDataSource(self.df_new_6t("blue", match))
        r_teams = self.cds_r.column_names[1:4]
        b_teams = self.cds_b.column_names[1:4]
        tasks = self.cds_r.data['task']
        plt_name = "Six Team Power Cells Placed: Match " + match

        self.plt_pc = plt.figure(title=plt_name, x_range=tasks,
                            plot_width=700, plot_height=300, toolbar_location=None, tools="hover",
                            tooltips="$name- @task: @$name")

        reds = bpalettes.Reds3
        self.plt_pc.vbar_stack(r_teams,
                               x=btransform.dodge('task', -0.17,range=self.plt_pc.x_range),
                               width=0.3, source=self.cds_r, legend_label=[" " + x for x in r_teams],
                               color=bpalettes.Reds3)
        self.plt_pc.vbar_stack(b_teams, x=btransform.dodge('task', 0.17, range=self.plt_pc.x_range), width=0.3, source=self.cds_b,
                         color=bpalettes.Blues3, legend_label=[" " + x for x in b_teams])
        return self.plt_pc

    def list_matches(self):
        return list(self.schedule.match.unique())

    def layout_6t(self, match):
        plot_6t = self.total_6t(match)
        match_sel = bmw.Select(title='Match', options=self.list_matches())
        match_sel.on_change('value', self.callback_6t)
        self.layout_6t = blay.row(match_sel, plot_6t)
        return self.layout_6t


