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
  { id: 0x00, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'startingPosition', display_name: 'Starting' },
  { id: 0x01, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'movedAuto', display_name: 'Moved IL' },
  { id: 0x02, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'crossOpponentSector', display_name: 'Crossed OS' },
  { id: 0x03, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'collided', display_name: 'Collided' },
  { id: 0x04, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'pickupPowerCellsT', display_name: 'Trench' },
  { id: 0x05, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'pickupPowerCellsS', display_name: 'Shield' },
  { id: 0x06, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'shootLower', display_name: 'Shoot Outer' },
  { id: 0x07, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'shootUpper', display_name: 'Shoot Lower' },
  { id: 0x08, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto,  task_name: 'shootInner', display_name: 'Shoot Inner' },
  
  { id: 0x09, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop,  task_name: 'defense', display_name: 'Defense' },
  { id: 0x0a, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop,  task_name: '', display_name: 'Defended Against' },
  { id: 0x0b, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop,  task_name: '', display_name: 'CP Rotation' },
  { id: 0x0c, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop,  task_name: '', display_name: 'CP Position' },
  { id: 0x0d, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: '', display_name: 'Loading' },
  { id: 0x0e, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: '', display_name: 'Ground' },
  { id: 0x0f, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: '', display_name: 'Shoot Outer' },
  { id: 0x10, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: '', display_name: 'Shoot Lower' },
  { id: 0x11, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop,  task_name: '', display_name: 'Shoot Inner' },
  { id: 0x12, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: '', display_name: 'Pass' },

  { id: 0x13, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'Disabled' },
  { id: 0x14, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'Temp. Disabled' },
  { id: 0x15, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'No Show' },
  { id: 0x16, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'Fall Over' },
  { id: 0x17, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'Climb' },
  { id: 0x18, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: '', display_name: 'Is Level' },
];