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
  { id: 11, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Starting' },
  { id: 12, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Moved IL' },
  { id: 13, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Crossed OS' },
  { id: 14, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Collided' },
  { id: 15, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Trench' },
  { id: 16, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Shield' },
  { id: 17, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Shoot Outer' },
  { id: 18, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Shoot Lower' },
  { id: 19, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.auto, task_name: 'Shoot Inner' },
  { id: 20, type: 'RATING', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Defense' },
  { id: 21, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'CP Rotation' },
  { id: 22, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'CP Position' },
  { id: 23, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Loading' },
  { id: 24, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Ground' },
  { id: 25, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Shoot Outer' },
  { id: 26, type: 'SCORE', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Shoot Lower' },
  { id: 27, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Shoot Inner' },
  { id: 28, type: 'COUNT', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.teleop, task_name: 'Pass' },
  { id: 29, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'Disabled' },
  { id: 30, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'Temp. Disabled' },
  { id: 31, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'No Show' },
  { id: 32, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'Fall Over' },
  { id: 33, type: 'ENUM', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'Climb' },
  { id: 34, type: 'BOOL', attempts: 0, task_id:0, successes: 0,  actor: actors.robot, phase: phases.endgame, task_name: 'Is Level' },
  
  
  
  
  
];