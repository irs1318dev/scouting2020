import { Hero } from './hero';
import { Measure } from './match';

export class EnumOption {
  value: number;
  name: string;
}

export const ENUMOPTIONS: {[key: string]: EnumOption[]  } = {
  "Starting": [{ value: 1, name: 'Load' }, { value: 2, name: 'Center' }, { value: 3, name: 'Goal' },],
  "Climb": [{ value: 1, name: 'Side' }, { value: 2, name: 'Center' }, { value: 3, name: 'Parked' },],
  "Defense": [{ value: 1, name: '0' }, { value: 2, name: '1' },{ value: 3, name: '2' }, { value: 4, name: '3' },],
  "Defended Against": [{ value: 1, name: '0' }, { value: 2, name: '1' },{ value: 3, name: '2' }, { value: 4, name: '3' },],
};


export const DOMAINOPTIONS: {[key: string]: EnumOption[]  } = {
  "stations": [{ value: 0, name: 'na' }, { value: 1, name: 'one' }, { value: 2, name: 'two' },{ value: 3, name: 'three' },],
  "alliances": [{ value: 1, name: 'na' }, { value: 2, name: 'blue' }, { value: 3, name: 'red' }],
  "phases": [
    { value: 1, name: 'na' }, 
    { value: 2, name: 'claims' }, 
    { value: 3, name: 'auto' },
    { value: 4, name: 'teleop' },
    { value: 5, name: 'finish' },],
  "actors": [
    { value: 1, name: 'na' }, 
    { value: 2, name: 'drive_team' }, 
    { value: 3, name: 'robot' },
    { value: 4, name: 'pilot' },
    { value: 5, name: 'human_player' },
    { value: 6, name: 'alliance' },
    { value: 7, name: 'team' },
    { value: 7, name: 'field' },],
};
