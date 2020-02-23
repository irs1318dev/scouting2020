"""Uses data to generate one team graphs.
"""
import bokeh.models as bk_models
import bokeh.plotting as plt
import bokeh.layouts as blay
import bokeh.models.widgets as bmw
import bokeh.palettes as bk_palettes


class OneTeam:

    def __init__(self, data):
        self.data = data
        self.cds = None
        self.pcplot = None
        self.layout = None
        self.tasks = None

    def callback_1t(self, attr, old, new):
        self.layout.children[1] = self.total_1t(new, self.tasks)

    def df_new_1t(self, team, tasks):
        self.tasks = tasks
        measures = self.data.enum_measures[
            (self.data.enum_measures.team == team) &
            (self.data.enum_measures.task.isin(tasks))].copy()

        # get matches
        grouped = measures.groupby(['match', 'task'])
        grouped = grouped.sum()
        grouped = grouped.drop(columns=grouped.columns[1:5])
        grouped = grouped['successes']
        df_unstacked = grouped.unstack()
        df_fil = df_unstacked.fillna(0)
        return df_fil

    def total_1t(self, team, tasks):
        self.cds = bk_models.ColumnDataSource(self.df_new_1t(team, tasks))
        tasks = self.cds.column_names
        tasks = tasks[1:]
        matches = self.cds.data['match']
        plt_title = "Team " + team
        num_tasks = len(tasks)
        if num_tasks == 1:
            colors = ['#5900b3']
        elif num_tasks == 2:
            colors = ['#5900b3', '#e6b800']
        else:
            colors = bk_palettes.Category20[len(tasks)]
        self.pcplot = plt.figure(x_range=matches, plot_height=250,
                                 title=plt_title, tools="hover",
                                 tooltips="$name: @$name")

        glyphs = self.pcplot.vbar_stack(tasks, x='match', width=0.4,
                               source=self.cds, color=colors)
        legend_items = [(tasks[i], [glyphs[i]]) for i in range(0, len(tasks), 1)]
        legend = bk_models.Legend(items=legend_items, location='center')
        self.pcplot.add_layout(legend, 'right')
        return self.pcplot

    def list_teams(self):
        return list(self.data.schedule.team.unique())

    def layout_1t(self, team, tasks):
        self.total_1t(team, tasks)
        team_sel = bmw.Select(title='Match', options=self.list_teams())
        team_sel.on_change('value', self.callback_1t)
        self.layout = blay.row(team_sel, self.pcplot)
        return self.layout

    def panel_1t(self, team, tasks):
        self.layout_1t(team, tasks)
        return bk_models.Panel(child=self.layout,
                               title='One Team Charts')
