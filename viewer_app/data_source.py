"""Gets data for viewer classes.
Meghana Annamaneni 2/17/2020
"""
import pandas as pd

import server.model.connection as smc
import server.model.event as sme

class DataSource:
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