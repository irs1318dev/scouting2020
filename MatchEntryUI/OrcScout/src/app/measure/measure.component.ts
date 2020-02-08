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

  public increment() {    
    this.measure.value = this.measure.value + 1;
  }
  
  public decrement() {
    this.measure.value = this.measure.value - 1;
  }

}
