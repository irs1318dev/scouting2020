import { Component, OnInit, HostListener } from '@angular/core';
import { Measure, MatchScoreCard, Team } from '../match';
import { alliances } from "../domain-tables/alliances";
import { HeroService } from '../hero.service';
import { stations } from '../domain-tables/stations';

@Component({
  selector: 'app-match-score-card',
  host: {
    class:'fuller-page',
    style: 'width:100%'
  },
  templateUrl: './match-score-card.component.html',
  styleUrls: ['./match-score-card.component.less']
})
export class MatchScoreCardComponent implements OnInit {

  matchScoreCard: MatchScoreCard;
  constructor(private heroService: HeroService) { }

  add(): 
    void{
      console.log("in add");
      this.heroService.saveMeasures();
    }
  
  @HostListener('window:beforeunload', ['$event']) 
  unloadNotification($event: any) {    
    this.heroService.saveMeasures();
  }
  
  ngOnInit() {
    this.matchScoreCard = new MatchScoreCard();
    this.matchScoreCard.selectedTeam = new Team();
    this.matchScoreCard.selectedTeam.name = "test team";
    this.matchScoreCard.selectedTeam.alliance = alliances.blue; 
    this.matchScoreCard.selectedTeam.station = stations.one; 
    this.getMeasures();
  }

  getMeasures(): void {
    this.heroService.getBlankMeasures()
        .subscribe(measures => this.matchScoreCard.score = measures);
  }

  resetMeasures(): void {    
    this.heroService.resetMeasures();
  }
}
