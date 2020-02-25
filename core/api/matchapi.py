import cherrypy

import core.data_access.match
import core.data_access.event
import core.models.tablet


class MatchApi(object):
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


    """
        Used by android
        """

    @cherrypy.expose
    def matchteamtask(self, match, team, task, phase, capability='', attempt=0,
                      success=0, cycle_time=0):
        """Writes a measure to the database.

        Args:
            match: (str) Match number, such as "007-q".
            team: (str) FRC team number
            task: (str) Task name (season specific) such as "placeGear"
            phase: (str) Portion of competition to which task applies,
                such as "claim", "auto", "teleop", etc,
            capability: "true" if task just records that team or robot
                has a capability to do something (may be used in pit
                scouting).
            attempt: (int) Number of attempts made to complete this
                task, successful or not.
            success: (int) Number of successful attempts made to
                complete this task.
            cycle_time: (int) Amount of time required to complete a
                task, in seconds.

        Returns: (str) "hi"
        """
        try:
            self.matchDal.insert_match_task(team, task, match,
                                            phase, capability,
                                            attempt, success,
                                            cycle_time)
        except KeyError as key:
            print("--- KeyError: " + str(key) + " ---")
            return 'KeyError: ' + str(key)
        return 'hi'

    """
        Used by android
        """

    @cherrypy.expose
    def matchteamtasks(self, team='error', match=-1):
        """ Returns measures for a single team in a single match

        Args:
            team: (str) FRC team number
            match: Competitiion match number, such as "001-q"

        Returns: (str) Pseudo JSON code. Measures are separated by
        carriage returns ("\n") and dach measure is a JSON object
        literal with keys "match", "team", "task", "phase", "actor",
        "measuretype", "capability", "attempts", "success", and
        "cycle_times".

        """
        if match == -1:
            match = self.eventDal.get_current_match()
        return (self.matchDal.match_team_tasks(match, team) +
                '{end}')

    @cherrypy.expose
    def updatescore(self, match, team, task, phase, capability='', attempt=0,
                      success=0, cycle_time=0):
        """Writes a measure to the database.

        Args:
            match: (str) Match number, such as "007-q".
            team: (str) FRC team number
            task: (str) Task name (season specific) such as "placeGear"
            phase: (str) Portion of competition to which task applies,
                such as "claim", "auto", "teleop", etc,
            capability: "true" if task just records that team or robot
                has a capability to do something (may be used in pit
                scouting).
            attempt: (int) Number of attempts made to complete this
                task, successful or not.
            success: (int) Number of successful attempts made to
                complete this task.
            cycle_time: (int) Amount of time required to complete a
                task, in seconds.

        Returns: (str) "hi"
        """
        try:
            self.matchDal.insert_match_task(team, task, match,
                                            phase, capability,
                                            attempt, success,
                                            cycle_time)
        except KeyError as key:
            print("--- KeyError: " + str(key) + " ---")
            return 'KeyError: ' + str(key)
        return 'hi'

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def score(self, team='error', match=-1):
        """ Returns measures for a single team in a single match

        Args:
            team: (str) FRC team number
            match: Competitiion match number, such as "001-q"

        Returns: (str) Pseudo JSON code. Measures are separated by
        carriage returns ("\n") and dach measure is a JSON object
        literal with keys "match", "team", "task", "phase", "actor",
        "measuretype", "capability", "attempts", "success", and
        "cycle_times".

        """
        if match == -1:
            match = self.eventDal.get_current_match()
        return self.matchDal.get_score(match, team)


    """
        Used by android
        """


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def matchteams(self, match=-1):
        """Gets string with teams assigned to match or competition.

        Args:
            match:
                (str) Can be set to -1 (default), "na", or to a
                match number, e.g., "001-q". Optional.

                If set to -1, returns team from current match specified
                in status table in database server. Eacha lliance will
                be a JSON string, with alliances separated by carriage
                returns ("\n"). The JSON string keys are "alliance"
                ("red" or "blue"), "match", "team1", "team2", and
                "team3".

                If set to a match number, ignores current match
                specified in status table and returns teams assigned
                to match number. The format of resulting test string
                is the same as if -1 is specified.

                If set to "na", returns a Python dictionary. The "match"
                key contains "na" and the "teams" key contains a list of
                FRC team numbers as strings, as well as the value "na".

        Returns: pseudo-JSON string or JSON string representing a
        Python dictionary.
        """
        if match == -1:
            match = self.eventDal.get_current_match()
        if match == 'na':
            return self.matchDal.pit_teams()
        return self.matchDal.match_teams(match)


    @cherrypy.expose
    @cherrypy.tools.json_out()
    def pitteams(self, match=-1):
        return self.matchDal.pit_teams()

    @cherrypy.expose
    def matches(self, event='na'):
        """Returns JSON list of matches.

        Args:
            event: The FIRST API event code.

        Returns: List contains 1 dictionary for each match. Each
        dictionary contains two keys: "match" and "event".
        """
        if event == 'na':
            event = core.data_access.event.EventDal.get_current_event()

        return core.data_access.event.EventDal.list_matches(event[1],
                                                        event[2])

