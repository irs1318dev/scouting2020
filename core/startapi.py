import cherrypy

import server.config as s_config
import core.models.tablet
import core.api.gameapi
import core.api.viewerapi
import core.api.scoutingapi
import core.api.teamapi
import core.api.eventapi
import core.api.tabletapi
import core.api.matchapi

if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0'})

    conf = {"/web": {'tools.staticdir.on': True,
                     'tools.staticdir.dir': s_config.web_base()}}

    cherrypy.tree.mount(core.api.viewerapi.ViewerApi(False), '/view', config=conf)
    cherrypy.tree.mount(core.api.gameapi.GameApi(), '/game', config=conf)
    cherrypy.tree.mount(core.api.teamapi.TeamApi(), '/team', config=conf)
    cherrypy.tree.mount(core.api.tabletapi.TabletApi(), '/tablet', config=conf)
    cherrypy.tree.mount(core.api.eventapi.EventApi(), '/event', config=conf)
    cherrypy.tree.mount(core.api.matchapi.MatchApi(), '/match', config=conf)
    cherrypy.quickstart(core.api.scoutingapi.ScoutingApi(), '/', config=conf)
