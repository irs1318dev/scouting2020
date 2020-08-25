import { Component, OnInit, Input } from '@angular/core';
import { Measure } from '../match';
import { HeroService } from '../hero.service';
import { EnumOption, ENUMOPTIONS } from '../enum-lookups';

@Component({
  selector: 'app-measure',
  templateUrl: './measure.component.html',
  styleUrls: ['./measure.component.less']
})

export class MeasureComponent implements OnInit {
  @Input() 
  measure: Measure;
  
  options: EnumOption[];

  constructor(private heroService: HeroService) { }
  
  ngOnInit() {
    this.heroService.getMeasure(this.measure.id).subscribe(measure => this.measure = measure);
    this.options = ENUMOPTIONS[this.measure.display_name];
  }
  iterateAttempts(numm: number){
    if(typeof this.measure.attempts === "number"){
      this.measure.attempts = this.measure.attempts + numm;
    }
  }

  public hit() {    
    this.iterateAttempts(1);
    this.measure.successes = this.measure.successes + 1;
  }
  
  public undoHit() {    
    if(this.measure.attempts > 0 && this.measure.successes > 0)
      this.iterateAttempts(-1);
    if(this.measure.successes > 0 && this.measure.successes > 0)
      this.measure.successes = this.measure.successes - 1;
  }
  
  public miss() {
    this.iterateAttempts(1);;
  }
  
  public undoMiss() {
    if(this.measure.attempts > 0 && this.measure.attempts > this.measure.successes)
      this.iterateAttempts(-1);
  }

}
