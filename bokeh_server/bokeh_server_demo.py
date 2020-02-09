"""Bokeh Server Demonstration
Stacy Irwin, 9 Feb 2020

A simple demonstration of dynamically charted scouting data useing
a Bokeh Server.

To run this demo:
1. Save this file and the 'test_evt2.pickle' file in the same folder.
2. Run this line from a PowerShell or Terminal prompt in that folder:

bokeh server --show bokeh_server_demo.py
"""

import pickle

import bokeh.io as bkio
import bokeh.layouts as bklayouts
import bokeh.models as bkmodels
import bokeh.models.annotations as bkannotations
import bokeh.models.widgets as bkwidgets
import bokeh.plotting as bkplotting
import pandas as pd

class ScoutData:
    """A class that contains scouting data as Pandas datframes.

    Attributes:
        measures: A DataFrame containing measures data
        schedule: A Dataframe containing a competition schedule
        teams: A Dataframe with a list of teams competing in the
            competition.

    Methods:
        task_mean_dataframe: DataFrame of mean values for a single task.
        get_task_list: List of all tasks in the ScoutData.measures
        dataframe.

    Object Creation:
        To create a ScoutData object, pass in the name of the pickle
        file as a string to the constructor. For example:
        sdata = ScoutData('test_evt2.pickle')
    """

    def __init__(self, fname):
        """Initializes ScoutData object."""
        with open(fname, 'rb') as file:
            dframes = pickle.load(file)
        self.measures = dframes['measures']
        self.schedule = dframes['schedule']
        self.teams = dframes['teams']

        # Convert team number from string to integer for better sorting
        self.measures['team_int'] = self.measures.team.astype('int32')

    def task_mean_dataframe(self, task, ascending=False):
        """DataFrame of mean values for a single task.

        Args:
            task: str, name of task
            ascending, bool, Teams in ascending order from bottom to top
                if TRUE. Optional, default is False.

        Returns: Pandas Dataframe with one row per team and mean values
            of successes, attempts, etc., for the specified task.
        """
        task_meas = self.measures[self.measures.task == str(task)]
        task_means = task_meas.groupby(['team']).mean()
        task_means.sort_values('team_int', inplace=True, ascending=ascending)
        return task_means

    def get_task_list(self):
        """Returns a list of all tasks in self.measures dataframe."""
        return list(pd.unique(self.measures.task))


def plot_team_hbar(task, source, ascending=False):
    """Returns a horizontal bar chart for a givent task.

    Args:
        task: str, name of task to plot.
        source: A Bokeh ColumnDataSource object containing the data
            to plot.
        ascending, bool, Teams in ascending order from bottom to top
            if TRUE. Optional, default is False.

    Returns: Bokeh Figure object.
    """
    p = bkplotting.figure(y_range=source.data['team'],
    plot_height=750, title=str(task) + ' Mean', toolbar_location=None,
    tools="")
    p.hbar(y='team', right='successes', source = source, height=0.5)
    return p

def dropdown_update(evt):
    """ Callback function that runs whenever user selects a task in webpage.
    """

    # IMPORTANT!!!!!!!!!!!!!!!!!!!!!
    # Change the plot's underlying data by changeing the data atribute
    #   of the plot's ColumnDataSource object.
    source.data = sdata.task_mean_dataframe(evt.item)

    # We should update the plot title while we're at it.
    plot.title.text = evt.item + ' Mean'


# Here is where the code starts executing.

# Create a dataframe for a single task
sdata = ScoutData('test_evt2.pickle')
default_task = 'shootLower'
source_df = sdata.task_mean_dataframe(default_task)

# Convert the dataframe to a ColumnDataSource object.
source = bkmodels.ColumnDataSource(source_df)

# Generate the plot.
plot = plot_team_hbar(default_task, source)

# Create a dropdown box with all of the tasks in the measures df
task_dropdown = bkwidgets.Dropdown(menu=sdata.get_task_list())
task_dropdown.on_click(dropdown_update)

# Add the plot and the dropdown box to the current webpage.
bkplotting.curdoc().add_root(bklayouts.column(task_dropdown, plot))

