import { alliances } from './domain-tables/alliances';
import { stations } from './domain-tables/stations';
import { actors } from './domain-tables/actors';
import { phases } from './domain-tables/phases';

export class Match {
    id: number;
    name: string
    teams: Team[];
}

export class Team {
    id: number;
    name: string;
    alliance: alliances;
    station: stations;
}

export class MatchScoreCard {
    match: Match;
    selectedTeam: Team;
    score: Measure[];
}

export class Measure {
    id: number;
    attempts: number;
    successes: number;
    display_name: string;
    task_name: string;
    type: string;
    task_id: number;
    actor: actors;
    phase: phases;
}