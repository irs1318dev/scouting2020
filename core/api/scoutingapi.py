import cherrypy

import core.config as c_config
import core.data_access.schedule
import core.data_access.setup
import core.api.viewerapi
import core.data_access.match
import core.data_access.event
import core.models.tablet


class ScoutingApi(object):
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
    def index(self):
        """Returns Scouting System start page.

        Start page displays current match and event, allows user to set
        current match, displays a table showing tablet pages, and includes
        links to other scouting system pages.

        Returns: (str) HTML text
        """
        out = open(c_config.web_sites("admin.html")).read()
        out = out.replace('{Match}', self.eventDal.get_current_match())
        out = out.replace('{Event}', self.eventDal.get_current_event()[1])
        out = out.replace('{Year}', self.eventDal.get_current_event()[2])
        return out

    @cherrypy.expose
    def setup(self):
        """Returns Scouting System setup page.

        Allows user to set event and contains links for server
        directions, entering the schedule manually, setting up a new
        database, and backing up data.

        Returns: (str) HTML text
        """
        out = open(c_config.web_sites("setup.html")).read()
        out = out.replace('{Event}', self.eventDal.get_current_event()[1])
        out = out.replace('{Year}', self.eventDal.get_current_event()[2])
        return out
