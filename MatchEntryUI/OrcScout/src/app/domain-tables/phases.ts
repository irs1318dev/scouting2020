export enum phases {
    na = 1,
    claims = 2,
    auto = 3,
    teleop = 4,
    finish = 5
}

export const PhasesLabel = new Map<number, string>([
    [phases.na, 'na'],
    [phases.claims, 'claims'],
    [phases.auto, 'auto'],
    [phases.teleop, 'teleop'],
    [phases.finish, 'finish']
  ]);