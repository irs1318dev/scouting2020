import bokeh.plotting as bk_plt
import bokeh.models as bk_models
import bokeh.layouts as bk_layouts


class OneTeam:

    def __init__(self, data):
        self.measures = data.measures
        self.schedule = data.schedule

    def callback_1t(self, attr, old, new):
        print('In callback for team:', new)
        self.layout.children[1] = self.plot_1t(new)

    def df_new_1t(self, team):
        df_matches = self.schedule[(self.schedule.team == team)]
        match_list = df_matches.match.unique()
        sorted_match = self.measures[self.measures.match.isin(match_list)]
        sorted_match = sorted_match[(sorted_match.team == team)]
        sorted_task = sorted_match[sorted_match.task.isin(['shootUpper',
                                                           'shootLower'])]
        grouped = sorted_task.groupby(['match', 'task'])
        grouped = grouped.sum()
        grouped = grouped.drop(columns=grouped.columns[1:5])
        df_unstacked = grouped.unstack()
        df_unstacked.columns = df_unstacked.columns.droplevel()
        df_fil = df_unstacked.fillna(0)
        return df_fil

    def plot_1t(self, team):
        self.cds = bk_models.ColumnDataSource(self.df_new_1t(team))
        col_names = self.cds.column_names
        tasks = col_names[1:3]
        matches = self.cds.data['match']
        plt_title = "Team " + team
        colors = ['#30678D', '#FDE724']
        self.pcplot = bk_plt.figure(x_range=matches, plot_height=250,
            title=plt_title, tools="hover", tooltips="$name: @$name")
        self.pcplot.vbar_stack(tasks, x='match', width=0.4,
            source=self.cds, color=colors,
            legend_label=[" " + x for x in tasks])
        return self.pcplot

    def list_teams(self):
        return list(self.schedule.team.unique())

    def layout_1t(self, team):
        plot_1t = self.plot_1t(team)
        team_sel = bk_models.Select(title='Team', options=self.list_teams())
        team_sel.on_change('value', self.callback_1t)
        self.layout = bk_layouts.row(team_sel, plot_1t)
        return self.layout

    def panel(self, team):
        layout = self.layout_1t(team)
        return bk_models.Panel(child=layout, title='One Team Charts')
