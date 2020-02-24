import cherrypy

import core.config as s_config
import core.models.tablet
import core.api.gameapi
import core.api.viewerapi
import core.api.scoutingapi
import core.api.teamapi
import core.api.eventapi
import core.api.tabletapi
import core.api.matchapi
import core.api.measuresapi



if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_host': '0.0.0.0',
         'server.socket_port': 8080})

    conf = {"/": {'tools.staticdir.on': True,
                  'tools.staticdir.dir': s_config.web_base(),
                  'tools.response_headers.on': True,
                  'tools.response_headers.headers': [('Access-Control-Allow-Origin', '*')]}}


    def secure_headers():
        cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"


    cherrypy.tools.secure_headers = cherrypy.Tool(
        'before_handler', secure_headers, None, priority=30)

    cherrypy.tree.mount(core.api.viewerapi.ViewerApi(False), '/view', config=conf)
    cherrypy.tree.mount(core.api.gameapi.GameApi(), '/game', config=conf)
    cherrypy.tree.mount(core.api.teamapi.TeamApi(), '/team', config=conf)
    cherrypy.tree.mount(core.api.measuresapi.MeasuresApi(), '/measure', config=conf)
    cherrypy.tree.mount(core.api.tabletapi.TabletApi(), '/tablet', config=conf)
    cherrypy.tree.mount(core.api.eventapi.EventApi(), '/event', config=conf)
    cherrypy.tree.mount(core.api.matchapi.MatchApi(), '/match', config=conf)
    cherrypy.tree.mount(core.api.scoutingapi.ScoutingApi(), '/', config=conf)
    cherrypy.engine.signals.subscribe()
    cherrypy.engine.start()
    cherrypy.engine.block()
