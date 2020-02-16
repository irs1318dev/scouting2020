import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';
import { phases } from '../domain-tables/phases';


@Component({
  selector: 'app-phase-endgame',
  templateUrl: './phase-endgame.component.html',
  styleUrls: ['./phase-endgame.component.less']
})
export class PhaseEndgameComponent implements OnInit {

  @Input()
  measures: Measure[];

  constructor() { }

  ngOnInit() {
  }

  getMeasure(measureName:string): Measure{
    return this.measures.find(c => c.task_name == measureName && c.phase == phases.endgame);
  }

}
