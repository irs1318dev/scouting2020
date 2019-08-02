import cherrypy

import server.scouting.tasks
import server.scouting.tablet


class Game(object):
    @cherrypy.expose
    def gamelayout(self):
        """Returns pseudo-JSON string with season-specific tasks

        Data formatted as JSON list of key-value objects.

        JSON keys:
            actor: Entity that completes task, such as robot, alliance,
            or team.
            category: Examples include Starting, Gear, Fuel, Climb, etc.
            newpart: true or false. Not sure what this is.
            observer: Where task is observed, such as match or pit.
            phase: Part of competition in which task occurs, such as
            auto, teleop, claim, or finish.
            position: "", 1, 2, 3, or waiting.
            tasks: Name of task, such as placeGear or pushTouchPad

        Returns: (str) pseudo-JSON text. The individual JSON
        dictionaries are separated by "\n" carriage return characters
        instead of being separated by commas and included in a list.
        """
        return server.scouting.sections.Observers().load()

    @cherrypy.expose
    def gametasks(self):
        """Returns pseudo-JSON string with season specific tasks

        JSON keys:
            actor: Entity that completes task, such as robot, alliance,
            or team.
            auto: datatype or "na" if task does not apply to auto
            claim: datatype or "na" if task does not apply to claim
            enums: Used when tablet UI displays a drop-down list for
                data entry. Contains list of options separated by '|',
                or "" empty string if drop-down list not used.
            finish: datatype or "na" if task does not apply to claim
            miss: ???
            success: ???
            task: name of task, such as placeGear or shootLowBoiler
            teleop: datatype or "na" if task does not apply to teleop

        Returns: (str) pseudo-JSON text. The individual JSON
        dictionaries are separated by "\n" carriage return characters
        instead of being separated by commas and included in a list.
        """
        return server.scouting.tasks.TaskDal.csvtasks()
