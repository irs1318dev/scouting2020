import os
import os.path

import pandas as pd
import bokeh.models as bmodels
import bokeh.plotting as plt
import bokeh.palettes as bpalettes
import bokeh.transform as btransform
import bokeh.models.widgets as bmw
import bokeh.io
import bokeh.layouts as blt
import pickle

import server.model.connection as smc
import server.config as sc
import server.model.event as sme
import server.view.bokeh_res

def read_pickle(pickle_file):
    testdata = pd.read_pickle(pickle_file)
    schedule = testdata["schedule"]
    mea = testdata["measures"]

    return schedule, mea

def read_df(df):
    return df

def cds_new_6t(alliance, match, mea, schedule):
    df_teams = schedule[(schedule.match == match)]
    teams_list = df_teams[(df_teams.alliance == alliance)].team.unique()
    sorted_team = mea[mea.team.isin(teams_list)]
    sorted_task = sorted_team[sorted_team.task.isin(['shootUpper', 'shootLower'])]
    grouped = sorted_task.groupby(['task', 'team'])
    grouped = grouped.sum()
    grouped = grouped.drop(columns=grouped.columns[1:5])
    df_unstacked = grouped.unstack()
    df_unstacked.columns = df_unstacked.columns.droplevel()
    df_fil = df_unstacked.fillna(0)
    df_fil.loc['Total PC', :] = list(df_fil.sum())
    return bmodels.ColumnDataSource(df_fil)


def total_6t(match, mea, schedule):
    cds_r = cds_new_6t("red", match, mea, schedule)
    cds_b = cds_new_6t("blue", match, mea, schedule)
    r_teams = cds_r.column_names[1:4]
    b_teams = cds_b.column_names[1:4]
    tasks = cds_b.data['task']
    plt_name = "Six Team Power Cells Placed: Match " + match

    plt_pc = plt.figure(title=plt_name, x_range=tasks,
                        plot_width=700, plot_height=300, toolbar_location=None, tools="hover",
                        tooltips="$name- @task: @$name")

    plt_pc.vbar_stack(r_teams, x=btransform.dodge('task', -0.17, range=plt_pc.x_range), width=0.3, source=cds_r,
                      color=bpalettes.Reds3, legend_label=[" " + x for x in r_teams])
    plt_pc.vbar_stack(b_teams, x=btransform.dodge('task', 0.17, range=plt_pc.x_range), width=0.3, source=cds_b,
                      color=bpalettes.Blues3, legend_label=[" " + x for x in b_teams])
    bokeh.io.show(plt_pc)

    return plt_pc
