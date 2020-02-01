import { Hero } from './hero';
import { Measure } from './match';

export const HEROES: Hero[] = [
  { id: 11, name: 'Dr Nice' },
  { id: 12, name: 'Narco' },
  { id: 13, name: 'Bombasto' },
  { id: 14, name: 'Celeritas' },
  { id: 15, name: 'Magneta' },
  { id: 16, name: 'RubberMan' },
  { id: 17, name: 'Dynama' },
  { id: 18, name: 'Dr IQ' },
  { id: 19, name: 'Magma' },
  { id: 20, name: 'Tornado' }
];

export const MEASURES: Measure[] = [
  { measure_id: 11, measure_type: 'ENUM', value: 0, measure_name: 'Dr Nice' },
  { measure_id: 12, measure_type: 'ENUM', value: 0, measure_name: 'Narco' },
  { measure_id: 13, measure_type: 'ENUM', value: 0, measure_name: 'Bombasto' },
  { measure_id: 14, measure_type: 'ENUM', value: 0, measure_name: 'Celeritas' },
  { measure_id: 15, measure_type: 'INT', value: 0, measure_name: 'Magneta' },
  { measure_id: 16, measure_type: 'INT', value: 0, measure_name: 'RubberMan' },
  { measure_id: 17, measure_type: 'INT', value: 0, measure_name: 'Dynama' },
  { measure_id: 18, measure_type: '', value: 0, measure_name: 'Dr IQ' },
  { measure_id: 19, measure_type: '', value: 0, measure_name: 'Magma' },
  { measure_id: 20, measure_type: '', value: 0, measure_name: 'Tornado' }
];

export const MEASURES2: {[key: string]: Measure } = {
  "11": { measure_id: 11, measure_type: 'ENUM', value: 0, measure_name: 'Dr Nice' },
  "12": { measure_id: 12, measure_type: 'ENUM', value: 0, measure_name: 'Narco' },
  "13": { measure_id: 13, measure_type: 'ENUM', value: 0, measure_name: 'Bombasto' },
  "14": { measure_id: 14, measure_type: 'ENUM', value: 0, measure_name: 'Celeritas' },
  "15": { measure_id: 15, measure_type: 'INT', value: 0, measure_name: 'Magneta' },
  "16": { measure_id: 16, measure_type: 'INT', value: 0, measure_name: 'RubberMan' },
  "17": { measure_id: 17, measure_type: 'INT', value: 0, measure_name: 'Dynama' },
  "18": { measure_id: 18, measure_type: '', value: 0, measure_name: 'Dr IQ' },
  "19": { measure_id: 19, measure_type: '', value: 0, measure_name: 'Magma' },
  "20": { measure_id: 20, measure_type: '', value: 0, measure_name: 'Tornado' }
};