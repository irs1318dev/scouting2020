import { Component, OnInit, HostListener, SimpleChanges } from '@angular/core';
import { Measure, MatchScoreCard, Team } from '../match';
import { alliances } from "../domain-tables/alliances";
import { HeroService } from '../hero.service';
import { EnumOption, DOMAINOPTIONS } from '../enum-lookups';
import { stations } from '../domain-tables/stations';
import { RedVBlue } from '../models/redVblue';
import { MatchService } from '../match.service';

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
  matchStarted: boolean;
  redVBlue: RedVBlue;
  stations: EnumOption[];
  alliances: EnumOption[];
  matchScoreCard: MatchScoreCard;
  constructor(private heroService: HeroService, private matchService: MatchService) { }

  add(): void{
      console.log("in add");
      // add method not implemented yet. 
      //this.heroService.saveMeasures();
  }
  
  @HostListener('window:beforeunload', ['$event']) 
  unloadNotification($event: any) {    
    this.heroService.saveMeasures();
  }
  
  ngOnInit() {
    this.matchStarted = false;
    this.getRedVBlue();
    this.stations = DOMAINOPTIONS['stations'];
    this.alliances = DOMAINOPTIONS['alliances'];
    this.matchScoreCard = new MatchScoreCard();
    this.matchScoreCard.selectedTeam = new Team();
    this.matchScoreCard.selectedTeam.alliance = alliances.na; 
    this.matchScoreCard.selectedTeam.station = stations.na; 
    this.getMeasures();
    this. getAllianceName();
  }
  
  getAllianceName(): void {
    if (this.matchScoreCard.selectedTeam.alliance === alliances.na || this.matchScoreCard.selectedTeam.station === stations.na)
    {
      this.matchScoreCard.selectedTeam.name = '';
    }
    else if (this.matchScoreCard.selectedTeam.alliance === alliances.red)
    {
      let team = this.redVBlue.red.find(c => c.station == this.matchScoreCard.selectedTeam.station);
      this.matchScoreCard.selectedTeam.name =team.team;
      this.matchScoreCard.match.name = team.match;
    }
    else if (this.matchScoreCard.selectedTeam.alliance === alliances.blue)
    {
      let team = this.redVBlue.blue.find(c => c.station == this.matchScoreCard.selectedTeam.station);
      this.matchScoreCard.selectedTeam.name = team.team;
      this.matchScoreCard.match.name = team.match;
    }
  }

  getRedVBlue(): void {
    this.matchService.getMatch(null)
        .subscribe(redVBlue => this.redVBlue= redVBlue);
  }

  getMeasures(): void {
    this.heroService.getBlankMeasures()
        .subscribe(measures => this.matchScoreCard.score = measures);
  }

  retreiveMeasures(): void {    
    this.matchStarted = true;
    this.heroService.startMatch(this.matchScoreCard.selectedTeam.name, this.matchScoreCard.match.name)
    .subscribe(measures => this.matchScoreCard.score = measures);
  }

  sendMeasures(): void {    
    this.matchStarted = false;
    this.heroService.postScore(this.matchScoreCard.selectedTeam.name, this.matchScoreCard.match.name)
    // WIP, does not yet  measures.  
  }
}
