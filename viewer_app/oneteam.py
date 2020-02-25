"""Uses data to generate one team graphs.
"""
import bokeh.models as bk_models
import bokeh.plotting as plt
import bokeh.layouts as blay
import bokeh.models.widgets as bmw
import pandas as pd


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
        measures = self.data.measures[
            (self.data.measures.team == team) &
            (self.data.measures.task.isin(tasks))].copy()
        measures.loc[measures.capability.isin(['Side', 'Center']),
                     'successes'] = 5
        measures.loc[measures.capability == 'Parked', 'successes'] = 2
        measures.loc[measures.capability == 'Side', 'task'] = 'climb_side'
        measures.loc[measures.capability == 'Center', 'task'] = 'climb_center'
        measures.loc[measures.capability == 'Parked', 'task'] = 'climb_parked'

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
        colors = ['purple', 'yellow']
        self.pcplot = plt.figure(x_range=matches, plot_height=250,
                                 title=plt_title, tools="hover",
                                 tooltips="$name: @$name")
        self.pcplot.vbar_stack(tasks, x='match', width=0.4,
                               source=self.cds, color=colors)
                               # legend_label=[" " + str(task) for task in tasks])
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
