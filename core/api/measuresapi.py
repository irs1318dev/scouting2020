import cherrypy
import simplejson

import core.config as c_config
import core.data_access.schedule
import core.data_access.setup
import core.api.viewerapi
import core.data_access.match
import core.data_access.event
import core.models.tablet


class MeasuresApi(object):
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
    def update(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = simplejson.loads(rawbody)
        # do_something_with(body)
        return "Updated %r." % (body,)