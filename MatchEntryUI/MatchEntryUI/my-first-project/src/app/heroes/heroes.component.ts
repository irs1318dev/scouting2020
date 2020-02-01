import { Component, OnInit } from '@angular/core';
import { Hero } from '../hero';
import { HEROES } from '../mock-heroes';
import { HeroService } from '../hero.service';
import { RedVBlue } from '../models/redVblue';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.less']
})

export class HeroesComponent implements OnInit {

  heroes: Hero[];
  redvBlue: RedVBlue;

  constructor(private heroService: HeroService) { }

  ngOnInit() {
    this.getHeroes();
    this.getRedVBlue();
  }

  getRedVBlue(): void {
    this.heroService.getRedVBlue()
        .subscribe(heroes => this.redvBlue = heroes);
  }

  getHeroes(): void {
    this.heroService.getHeroes()
        .subscribe(heroes => this.heroes = heroes);
  }
}