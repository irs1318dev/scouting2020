import { Hero } from './hero';
import { Measure } from './match';

export class EnumOption {
  value: number;
  name: string;
}

export const ENUMOPTIONS: {[key: string]: EnumOption[]  } = {
  "Starting": [{ value: 1, name: 'Load' }, { value: 2, name: 'Center' }, { value: 3, name: 'Goal' },],
};
