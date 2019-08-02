import cherrypy

import server.config as s_config
import core.models.tablet
import core.api.gameapi
import core.api.viewerapi
import core.api.scoutingapi

if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0'})

    conf = {"/web": {'tools.staticdir.on': True,
                     'tools.staticdir.dir': s_config.web_base()}}

    cherrypy.tree.mount(core.api.viewerapi.Viewer(False), '/view', config=conf)
    cherrypy.tree.mount(core.api.gameapi.Game(), '/game', config=conf)
    cherrypy.quickstart(core.api.scoutingapi.Scouting(), '/', config=conf)
