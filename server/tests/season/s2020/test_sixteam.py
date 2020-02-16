import server.model.connection as smc
import server.model.event as sme
import pandas as pd

sme.EventDal.set_current_event('test_event_2', 2020)
conn = smc.pool.getconn()
    sql = """
        SELECT *
            FROM vw_measures
    """
    measures = pd.read_sql(sql, conn)
sql = """
        SELECT *
            FROM vw_measures
    """
    schedule = pd.read_sql(sql, conn, params=[team])
    smc.pool.putconn(conn)
