import cherrypy

import core.data_access.match
import core.data_access.event
import core.models.tablet
import core.config as c_config


class TabletApi(object):
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
    def databaseset(self):
        core.data_access.setup.setup()
        return open(c_config.web_sites("reset.html")).read()

    @cherrypy.expose
    def addresslist(self):
        connected, unlinked = self.alltablets.get_address()
        out = '<h3>Connected Ip Addresses:</h3>' + str(connected)
        out += '<h3>Unlinked Ip Addresses:</h3>' + str(unlinked)
        return out

    """
    Used by android
    """

    @cherrypy.expose
    def tablets(self):
        out = open(c_config.web_sites("tablets.txt")).read()
        out = self.alltablets.inserttablets(out)
        out = out.replace('{Match=""}',
                          '{Match="' + self.eventDal.get_current_match() + '"}')
        return out

    """
    Used by android
    """

    @cherrypy.expose
    def tablet(self, status, ip=-1):
        newtablet = core.models.tablet.Tablet(status.split(':')[0], status.split(':')[1], ip)

        if self.alltablets.settablet(newtablet):
            self.eventDal.set_next_match(self.eventDal.get_current_match())

        return self.eventDal.get_current_match()

    @cherrypy.expose
    def matchcurrent(self, match):
        self.tablet('TestSystem:Reset')
        self.eventDal.set_current_match(match)
        return open(c_config.web_sites("reset.html")).read()
