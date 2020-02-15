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
  { measure_id: 11, measure_type: 'ENUM', attempts: 0, successes: 0, measure_name: 'Starting' },
  { measure_id: 12, measure_type: 'BOOL', attempts: 0, successes: 0, measure_name: 'Moved IL' },
  { measure_id: 13, measure_type: 'BOOL', attempts: 0, successes: 0, measure_name: 'Crossed OS' },
  { measure_id: 14, measure_type: 'BOOL', attempts: 0, successes: 0, measure_name: 'Collided' },
  { measure_id: 15, measure_type: 'COUNT', attempts: 0, successes: 0, measure_name: 'Trench' },
  { measure_id: 16, measure_type: 'COUNT', attempts: 0, successes: 0, measure_name: 'Shield' },
  { measure_id: 17, measure_type: 'COUNT', attempts: 0, successes: 0, measure_name: 'Shoot Outer' },
  { measure_id: 18, measure_type: 'COUNT', attempts: 0, successes: 0, measure_name: 'Shoot Lower' },
  { measure_id: 19, measure_type: 'BOOL', attempts: 0, successes: 0, measure_name: 'Shoot Inner' },
];