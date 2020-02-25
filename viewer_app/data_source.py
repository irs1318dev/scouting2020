"""Gets data for viewer classes.
Meghana Annamaneni 2/17/2020
Revised by Stacy Irwin 2/17/2020

Contents
--------
    DataSource: A class that can extract scouting data from either the
        scouting system's SQL database, or from a Python pickle file.

All classes that create plots or tables for the viewer_app should use
DataSource to connect to the scouting SQL database or to a Python pickle
data file. In general, a DataSource will be passed to the plotting
class's constructor as an argument.
"""
import pickle

import pandas as pd

import server.model.connection as smc
import server.model.event as sme


class DataSource:
    """Provides DataFrames for plotting to viewer_app classes.

    If no arguments are passed to the constructor, DataSource will retrieve
    data directly from the scouting database. Other options are to pass
    a file name or both an event name and the season.
        Constructor Arguments:
            fname: Optional, str. If specified, data will be loaded from a
                Python pickle file. fname must be a path or filename that
                can be used with the Python `open()` built-in function. If
                omitted, DataSource will load scouting data from the
                scouting database.
            event: Optional, str. A string used to identify the competition.
                Usually the FIRST API event code. If not specified,
                DataSource will connect directly to the scouting system SQL
                database.
            season: Optional, str. A string identifying the four-digit year
                for the specific game being scouted. E.g., '2020' refers to
                *Infinite Recharge* and `2019` refers to *Deep Space*.

        Attributes:
            measures: Pandas DataFrame containing detailed scouting data for
                each team and match.
            schedule: Pandas DataFrame containing the match schedule
            teams: Pandas DataFrame with list of teams participating in
                    competition
            event: str, FIRST API event code for event
            season: str, 4-digit year denoting the season
            fname: str, name of file from which data was loaded, or None if
                data loaded directly from scouting database.
            from_sql: bool, True if loaded from database, False otherwise

        Methods:
            refresh(): Reload scouting data from the source, either a file
                or the scouting database.
            write_file(): Write the scouting data to a Python pickle file.
    """
    def __init__(self, fname=None, event=None, season=None):
        """Initializes a DataSource object."""
        self.measures = None
        self.schedule = None
        self.teams = None
        self.status = None
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
        """Loads data from a Python pickle file."""
        with open(self.fname, 'rb') as data_file:
            data = pickle.load(data_file)
        self.measures = data['measures']
        self.schedule = data['schedule']
        self.teams = data['teams']
        self.event = data['event']
        self.season = data['season']
        self.status = data['status']

    def _load_from_sql(self):
        """Connects to the scouting database and creates DataFrames."""
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
        SELECT * FROM vw_schedule;"""
        self.schedule = pd.read_sql(sql, conn)

        sql = """
        SELECT * FROM teams
            WHERE teams.name IN
                (SELECT team FROM schedules WHERE event_id = %s);"""
        teams = pd.read_sql(sql, conn, params=[str(evt_id)])

        sql = """
        SELECT * FROM vw_num_matches;"""
        num_matches = pd.read_sql(sql, conn)
        self.teams = pd.concat([teams, num_matches], axis=1)

        sql = """
        SELECT * FROM vw_status_date;"""
        self.status = pd.read_sql(sql, conn)

        # Return connection to pool.
        smc.pool.putconn(conn)

    def refresh(self, fname=None):
        """Refreshes data by reconnecting to the database or to a file.

        Args:
            fname: A Python style filename or path. fname must work with
                Python's built-in open() function.
        """
        if fname is not None:
            self.fname = fname
        if self.from_sql:
            self._load_from_sql()
        else:
            self._load_from_file()

    def write_file(self, fname=None):
        """Writes all data to a Python pickle file.

        Args:
            fname: A Python style filename or path. fname must work with
                Python's built-in open() function.
        """
        data = {'measures': self.measures, 'schedule': self.schedule,
                'teams': self.teams, 'event': self.event,
                'season': self.season, 'status': self.status}

        with open(fname, 'wb') as data_file:
            pickle.dump(data, data_file)
