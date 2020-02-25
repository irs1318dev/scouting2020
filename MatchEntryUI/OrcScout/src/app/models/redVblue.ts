import { alliances } from '../domain-tables/alliances';
import { stations } from '../domain-tables/stations';

    export interface Alliance {
        team: string;
        match: string;
        alliance: alliances;
        station: stations;
    }

    export interface RedVBlue {
        red: Alliance[];
        blue: Alliance[];
    }

    export interface ScoreRecord {
        match: string;
        team: string;
        task: string;
        phase: string;
        actor: string;
        measuretype: string;
        capability: any;
        attempts: number;
        successes: number;
        cycle_times: number;
    }
