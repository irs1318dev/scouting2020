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
