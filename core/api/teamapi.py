import cherrypy

from server.model.connection import pool
import core.data_access.match
import core.data_access.event
import core.models.tablet


class TeamApi(object):
    def __init__(self, match_dal=None, event_dal=None, all_tablets=None):
        if match_dal is None:
            self.matchDal = core.data_access.match.MatchDal()
        else:
            self.matchDal = match_dal
        if event_dal is None:
            self.eventDal = core.data_access.event.EventDal()
        else:
            self.eventDal = event_dal
        if all_tablets is None:
            self.alltablets = core.models.tablet.TabletList()
        else:
            self.alltablets = all_tablets

    @cherrypy.expose()
    def team_match(team):
        sql = '''
              SELECT schedules.match FROM schedules
              INNER JOIN status ON schedules.event_id = status.event_id WHERE team = %s
              ORDER BY schedules.match;'''
        conn = pool.getconn()
        curr = conn.cursor()
        curr.execute(sql, [team])
        matches = [x[0] for x in curr.fetchall()]
        pool.putconn(conn)
        return matches

    @cherrypy.expose
    def teamname(self, team):
        return self.eventDal.team_long_name(team)
