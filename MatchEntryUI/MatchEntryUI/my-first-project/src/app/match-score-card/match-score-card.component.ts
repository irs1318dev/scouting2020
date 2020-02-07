import { Component, OnInit, HostListener } from '@angular/core';
import { Measure } from '../match';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-match-score-card',
  templateUrl: './match-score-card.component.html',
  styleUrls: ['./match-score-card.component.less']
})
export class MatchScoreCardComponent implements OnInit {

  measures: Measure[];
  constructor(private heroService: HeroService) { }

  
  @HostListener('window:beforeunload', ['$event']) 
  unloadNotification($event: any) {    
    this.heroService.saveMeasures();
  }
  
  ngOnInit() {
    this.getMeasures();
  }

  getMeasures(): void {
    this.heroService.getBlankMeasures()
        .subscribe(measures => this.measures = measures);
  }

  resetMeasures(): void {    
    this.heroService.resetMeasures();
  }

  getMeasure(measureName:string): Measure{
    return this.measures.find(c => c.measure_name == measureName);
  }
}
