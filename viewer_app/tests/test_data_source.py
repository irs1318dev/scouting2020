import os
import os.path

import pandas as pd

import viewer_app.data_source as app_data

test_event_name = 'test_event_2'
test_season = '2020'
test_file_name = r'\data_write_test.pickle'


def test_data_source():
    data = app_data.DataSource(event=test_event_name, season=test_season)
    assert isinstance(data, app_data.DataSource)
    assert isinstance(data.measures, pd.DataFrame)
    assert data.measures.shape[0] > 1000
    assert data.measures.shape[1] == 20

    assert isinstance(data.schedule, pd.DataFrame)
    assert isinstance(data.teams, pd.DataFrame)
    assert data.teams.shape[1] == 7
    assert data.teams.shape[0] > 20

    assert data.event == test_event_name
    assert data.season == test_season


def test_write_file():
    path = os.path.abspath(__file__)
    for _ in range(4):
        path = os.path.dirname(path)
    data = app_data.DataSource(event=test_event_name, season=test_season)
    fpath = path + test_file_name
    data.write_file(fpath)
    file_data = app_data.DataSource(fpath)
    os.remove(fpath)
    assert isinstance(file_data, app_data.DataSource)
    assert file_data.event == test_event_name
    assert file_data.season == test_season
    assert not file_data.from_sql
    assert isinstance(file_data.status, pd.DataFrame)

