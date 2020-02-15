import cherrypy
from cherrypy.lib.static import serve_file
import os.path
import core.data_access as cda
import core.config as s_config
import server.scouting.export
import core.data_access.event as event
import core.data_access.match as match
import server.season.s2018.viewer as graphing
import server.view.excel as excel
import server.scouting.export as export
import server.season.s2019.view.updater as u


class ViewerApi:
    def __init__(self, alone=True):
        self.alone = alone

    @cherrypy.expose
    def index(self):
        out = open(s_config.web_sites("view.html")).read()

        if self.alone:
            out = out.replace('{Back}', '')
        else:
            out = out.replace('{Back}', '<h3><a href="/">Scouting Director</a></h3>')
        out = out.replace('{Match}', event.EventDal.get_current_match())

        return out

    @cherrypy.expose
    def backup(self):
        export.ExportBackup.run_backup(event.EventDal.get_current_event()[1])
        return 'Success. <a href="/view">Viewer</a>'

    @cherrypy.expose
    def updateAllGraphs(self):
        u.update_graph()

    @cherrypy.expose
    def output(self):
        excel.write_to_excel(excel.rnk_rpt2018a)
        return 'Success. <a href="/view">Viewer</a>'

    @cherrypy.expose
    def restore(self, path):
        self.export.run_restore(path)
        return open(s_config.web_sites("reset.html")).read()

    @cherrypy.expose
    def teamplan(self, team='1318'):
        match_number = '001-q'
        matches = list()

        while '""' not in match.MatchDal.match_teams(match_number) and '130' not in match_number:
            if team in cda.match.MatchDal.match_teams(match_number):
                matches.append(match_number)

            next_match_number = int(match_number.split('-')[0]) + 1
            match_number = "{0:0>3}-q".format(next_match_number)

        out = ''
        for match_number in matches:
            out += '<a href="matchplan?match={M}">{M}</a> '
            out = out.replace('{M}', match_number)
        print(out)
        return out

    # todo: make a part of the system. doesn't work because graphing.py is no longer used. To start look into SQL and talk to Akhil
    # previously manually added match and 6 teams to system and manually graphed the data
    # @cherrypy.expose
    # def customplan(self, red1, red2, red3, blue1, blue2, blue3):
    #     out = open(s_config.web_sites('graphing.html')).read()
    #     teams = [red1, red2, red3, blue1, blue2, blue3]
    #     out = out.replace('{Match}', 'Custom')
    #     out = out.replace('{Schedule}', str(teams))
    #     out = out.replace('{After}', 'Updated: ' + event.EventDal.get_current_match())
    #
    #     return out.replace('{Data}', graphing.graph_match(teams))

    def teamsList(self, match_number):
        teams = list()
        for data in match.MatchDal.match_teams(match_number).split(','):
            if 'team' in data:
                teams.append(data.split(':')[1].split('"')[1])
        return teams


class Start:
    @cherrypy.expose
    def index(self):
        return open(s_config.web_sites("resetView.html"))
