export class Match {
    match_id: number;
    match_number: number;
    teams: Team[];
}

export class Team {
    team_id: number;
    team_name: string;
}

export class MatchScoreCard {
    match_id: number;
    match_number: number;
    selectedTeam: Team;
    score: Measure[];
}

export class Measure {
    measure_id: number;
    value: number;
    measure_name: string;
    measure_type: string;
}