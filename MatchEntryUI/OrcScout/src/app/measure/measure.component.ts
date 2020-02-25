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

  public hit() {    
    this.measure.attempts = this.measure.attempts + 1;
    this.measure.successes = this.measure.successes + 1;
  }
  
  public undoHit() {    
    if(this.measure.attempts > 0 && this.measure.successes > 0)
      this.measure.attempts = this.measure.attempts - 1;
    if(this.measure.successes > 0 && this.measure.successes > 0)
      this.measure.successes = this.measure.successes - 1;
  }
  
  public miss() {
    this.measure.attempts = this.measure.attempts + 1;
  }
  
  public undoMiss() {
    if(this.measure.attempts > 0 && this.measure.attempts > this.measure.successes)
      this.measure.attempts = this.measure.attempts - 1;
  }

}
