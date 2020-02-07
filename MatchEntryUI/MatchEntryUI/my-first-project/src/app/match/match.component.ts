import { Component, OnInit } from '@angular/core';
import { HeroService } from '../hero.service';
import { RedVBlue } from '../models/redVblue';
import { MatchService } from '../match.service';

@Component({
  selector: 'app-match',
  templateUrl: './match.component.html',
  styleUrls: ['./match.component.less']
})
export class MatchComponent implements OnInit {

  redvBlue: RedVBlue;
  match: string;

  constructor(private matchService: MatchService) { }

  ngOnInit() {
    this.getRedVBlue();
  }

  getRedVBlue(): void {
    this.matchService.getRedVBlue(this.match)
        .subscribe(heroes => this.redvBlue = heroes);
  }
}
