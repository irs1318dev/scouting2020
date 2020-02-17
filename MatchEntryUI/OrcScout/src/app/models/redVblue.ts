

    export interface Red {
        team: string;
        match: string;
    }

    export interface Blue {
        team: string;
        match: string;
    }

    export interface RedVBlue {
        red: Red[];
        blue: Blue[];
    }
