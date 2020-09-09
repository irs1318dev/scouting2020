import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';
import { phases } from '../domain-tables/phases';


@Component({
  selector: 'app-phase-finish',
  templateUrl: './phase-finish.component.html',
  styleUrls: ['./phase-finish.component.less']
})
export class PhaseEndgameComponent implements OnInit {

  @Input()
  measures: Measure[];

  constructor() { }

  ngOnInit() {
  }

  getMeasure(measureName:string): Measure{
    return this.measures.find(c => c.display_name == measureName && c.phase == phases.finish);
  }

}
