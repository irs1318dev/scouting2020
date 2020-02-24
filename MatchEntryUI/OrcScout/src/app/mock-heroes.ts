import { Hero } from './hero';
import { Measure } from './match';
import { actors } from './domain-tables/actors';
import { phases } from './domain-tables/phases';

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
  { id: 11, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'startingPosition', display_name: 'Starting' },
  { id: 12, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'movedAuto', display_name: 'Moved IL' },
  { id: 13, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'crossOpponentSector', display_name: 'Crossed OS' },
  { id: 14, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'collided', display_name: 'Collided' },
  { id: 15, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'pickupPowerCellsT', display_name: 'Trench' },
  { id: 16, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'pickupPowerCellsS', display_name: 'Shield' },
  { id: 17, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'shootLower', display_name: 'Shoot Outer' },
  { id: 18, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'shootUpper', display_name: 'Shoot Lower' },
  { id: 19, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'shootInner', display_name: 'Shoot Inner' },
];