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
