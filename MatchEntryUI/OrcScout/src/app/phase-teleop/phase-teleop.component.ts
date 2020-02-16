import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';
import { phases } from '../domain-tables/phases';

@Component({
  selector: 'app-phase-teleop',
  templateUrl: './phase-teleop.component.html',
  styleUrls: ['./phase-teleop.component.less']
})

export class PhaseTeleopComponent implements OnInit {

  @Input()
  measures: Measure[];

  constructor() { }

  ngOnInit() {
  }

  getMeasure(measureName:string): Measure{
    return this.measures.find(c => c.task_name == measureName && c.phase == phases.teleop);
  }

}
