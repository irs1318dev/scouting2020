"""
Repository of polls that uses in-memory objects, no serialization.
Used for testing only.
"""

from . import Poll, Choice, PollNotFound, Match
from . import _load_samples_json, _load_matches_json

class Repository(object):
    """In-Memory repository."""
    def __init__(self, settings):
        """Initializes the repository. Note that settings are not used."""
        self.name = 'In-Memory'
        self.index = {}
        self.matches = {}

    def get_polls(self):
        """Returns all the polls from the repository."""
        return self.index.values()

    def get_poll(self, poll_key):
        """Returns a poll from the repository."""
        poll = self.index.get(poll_key)
        if poll is None:
            raise PollNotFound()
        return poll

    def increment_vote(self, poll_key, choice_key):
        """Increment the choice vote count for the specified poll."""
        poll = self.get_poll(poll_key)
        for choice in poll.choices:
            if choice.key == choice_key:
                choice.votes += 1
                break

    def add_sample_polls(self):
        """Adds a set of polls from data stored in a samples.json file."""
        poll_key = 0
        choice_key = 0

        for sample_poll in _load_samples_json():
            poll = Poll(str(poll_key), sample_poll['text'])
            for sample_choice in sample_poll['choices']:
                poll.choices.append(Choice(str(choice_key), sample_choice))
                choice_key += 1

            self.index[str(poll_key)] = poll
            poll_key += 1

    def get_matchs(self):
        """Returns all the matchs from the repository."""
        return self.matches.values()

    def get_match(self, match_key):
        """Returns a match from the repository."""
        match = self.matches.get(match_key)
        if match is None:
            raise matchNotFound()
        return match

    def add_match_matchs(self):
        """Adds a set of matchs from data stored in a samples.json file."""
        match_key = 0
        choice_key = 0

        for sample_match in _load_matches_json():
            match = Match(str(match_key), sample_match)
            self.matches[str(match_key)] = match
            match_key += 1
