export enum alliances {
    na = 1,
    blue = 2,
    red = 3
}

export enum stations {
    na = 1,
    one = 2,
    two = 3,
    three = 4
}

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
    measure_id: number;
    attempts: number;
    successes: number;
    measure_name: string;
    measure_type: string;
}