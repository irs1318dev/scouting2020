import { Injectable, HostListener } from '@angular/core';
import { Hero } from './hero';
import { Measure } from './match';
import { HEROES, MEASURES } from './mock-heroes';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';

@Injectable({
  providedIn: 'root',
})
export class HeroService {

  measures: Measure[];
  constructor(private messageService: MessageService) { }
    
  getHeroes(): Observable<Hero[]> {
    // TODO: send the message _after_ fetching the heroes
    this.messageService.add('HeroService: fetched heroes');
    return of(HEROES);
  }

  getHero(id: number): Observable<Hero> {
    // TODO: send the message _after_ fetching the hero
    this.messageService.add(`HeroService: fetched hero id=${id}`);
    return of(HEROES.find(hero => hero.id === id));
  }

  saveMeasures(): void {
    if (this.measures == null || this.measures == null)
    {
      localStorage.removeItem("measures");
      return;
    }
    localStorage.setItem("measures", JSON.stringify(this.measures));
  }

  private populateMeasures() {
    if (this.measures == null || this.measures == undefined)
    {
      if (localStorage.getItem("measures")) {
        this.measures = JSON.parse(localStorage.getItem("measures")) as Measure[];
      }
      else
      {
        this.measures = MEASURES;
      }
    }
  }

  getMeasure(id: number): Observable<Measure> {
    // TODO: send the message _after_ fetching the hero
    this.messageService.add(`HeroService: fetched measure id=${id}`);
    this.populateMeasures();
    return of(this.measures.find(measure => measure.measure_id === id));
  }

  getBlankMeasures(): Observable<Measure[]> {
    this.messageService.add('HeroService: fetched Measures');
    this.populateMeasures();

    return of(this.measures);
  }
}