import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-measure',
  templateUrl: './measure.component.html',
  styleUrls: ['./measure.component.less']
})

export class MeasureComponent implements OnInit {
  @Input() 
  measure: Measure;

  constructor(private heroService: HeroService) { }

  ngOnInit() {
    this.heroService.getMeasure(this.measure.measure_id).subscribe(measure => this.measure = measure);
  }

  public hit() {    
    this.measure.attempts = this.measure.attempts + 1;
    this.measure.successes = this.measure.successes + 1;
  }
  
  public undoHit() {    
    this.measure.attempts = this.measure.attempts - 1;
    this.measure.successes = this.measure.successes - 1;
  }
  
  public miss() {
    this.measure.attempts = this.measure.attempts + 1;
  }
  
  public undoMiss() {
    this.measure.attempts = this.measure.attempts - 1;
  }

}
