"""Gets data for viewer classes.
Meghana Annamaneni 2/17/2020
Stacy Irwin 2/17/2020

Contents
--------
    DataSource: A class that can extract scouting data from either the
        scouting system's SQL database, or from a Python pickle file.
"""
import pickle

import pandas as pd

import server.model.connection as smc
import server.model.event as sme


class DataSource:
    def __init__(self, fname=None, event=None, season=None):
        self.measures = None
        self.schedule = None
        self.teams = None
        self.event = event
        self.season = season
        self.fname = fname
        self.from_sql = False

        if self.fname is not None:
            self._load_from_file()
        else:
            self.from_sql = True
            self._load_from_sql()

    def _load_from_file(self):
        with open(self.fname, 'rb') as data_file:
            data = pickle.load(data_file)
        self.measures = data['measures']
        self.schedule = data['schedule']
        self.teams = data['teams']
        self.event = data['event']
        self.season = data['season']

    def _load_from_sql(self):
        if self.event is not None and self.season is not None:
            sme.EventDal.set_current_event(self.event, self.season)

        # Load measures data
        conn = smc.pool.getconn()
        sql = "SELECT * FROM vw_measures;"
        self.measures = pd.read_sql(sql, conn)

        evt = sme.EventDal.get_current_event()
        evt_id = evt[0]
        self.event = evt[1]
        self.season = evt[2]

        sql = """
        SELECT * FROM schedules
            WHERE event_id=%s
            ORDER BY match, alliance;"""
        self.schedule = pd.read_sql(sql, conn, params=[str(evt_id)])

        sql = """
        SELECT * FROM teams
            WHERE teams.name IN
                (SELECT team FROM schedules WHERE event_id = %s);"""
        self.teams = pd.read_sql(sql, conn, params=[str(evt_id)])
        smc.pool.putconn(conn)

    def refresh(self, fname=None):
        if fname is not None:
            self.fname = fname
        if self.from_sql:
            self._load_from_sql()
        else:
            self._load_from_file()

    def write_file(self, fname = None):
        data = {'measures': self.measures, 'schedule': self.schedule,
                'teams': self.teams, 'event': self.event,
                'season': self.season}

        with open(fname, 'wb') as data_file:
            pickle.dump(data, data_file)

