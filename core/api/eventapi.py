import cherrypy

import core.data_access.match
import core.data_access.event
import core.models.tablet
import core.config as c_config
import core.data_access.schedule


class EventApi(object):
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


    @cherrypy.expose
    def eventfind(self, event, year):
        self.eventDal.set_current_event(event, year)
        self.eventDal.set_current_match('001-q')
        core.data_access.schedule.insert_sched(event, year, 'qual')
        return open(c_config.web_sites("reset.html")).read()

    @cherrypy.expose
    def eventcurrent(self, event, year):
        print("/n=====", event, year, "=====")
        self.eventDal.set_current_event(event, year)
        return open(c_config.web_sites("reset.html")).read()
