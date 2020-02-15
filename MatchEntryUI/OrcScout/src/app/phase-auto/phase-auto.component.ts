import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';

@Component({
  selector: 'app-phase-auto',
  templateUrl: './phase-auto.component.html',
  styleUrls: ['./phase-auto.component.less']
})
export class PhaseAutoComponent implements OnInit {

  @Input()
  measures: Measure[];

  constructor() { }

  ngOnInit() {
  }

  getMeasure(measureName:string): Measure{
    return this.measures.find(c => c.task_name == measureName);
  }
}
