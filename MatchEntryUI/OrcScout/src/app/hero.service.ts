import { Injectable, HostListener } from '@angular/core';
import { Hero } from './hero';
import { Measure } from './match';
import { HEROES, MEASURES } from './mock-heroes';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { RedVBlue } from './models/redVblue';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Match } from './match';
import { MatchScoreCardComponent } from './match-score-card/match-score-card.component';


import { Component, OnInit, Input } from '@angular/core';



@Injectable({
  providedIn: 'root',
})


export class HeroService {

  measures: Measure[];
  constructor(private http: HttpClient, private messageService: MessageService) { }
  
  private heroesUrl = 'http://localhost:8080/match/matchteams';  // URL to web api

  private log(message: string) {
    this.messageService.add(`HeroService: ${message}`);
  }
    /**
   * Handle Http operation that failed.
   * Let the app continue.
   * @param operation - name of the operation that failed
   * @param result - optional value to return as the observable result
   */
  private handleError<T> (operation = 'operation', result?: T) {
    return (error: any): Observable<T> => {

      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    };
  }

  getRedVBlue(): Observable<RedVBlue> {
    return this.http.get<RedVBlue>(this.heroesUrl)
      .pipe(
        tap(_ => this.log('fetched heroes')),
        catchError(this.handleError<RedVBlue>('getHeroes'))
      );
  }

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

  clearMeasures(): void {
    if (this.measures == null || this.measures == null)
    {
      localStorage.removeItem("measures");
      return;
    }
    localStorage.setItem("measures", JSON.stringify(this.measures));
  }

  saveMeasures(): void {
    console.log("why not");
    {
      for(let i=0;i<this.measures.length ;i++){
        // how do we get the current team? 
        // how do we get the current match number?
        let thing = new String("/match/matchteamtask?match=" + Match.id + "&team=" + MatchScoreCardComponent.MatchScoreCard.selectedTeam + "&task=" + this.measures[i].task_name + "&phase=" + this.measures[i].phase);  
      //  if(!measure.capability.isEmpty() && !measure.capability.equals("0")) s += "&capability=" + measure.capability;
        if(this.measures[i].successes != 0) thing += "&success=" + this.measures[i].successes;
        if(this.measures[i].attempts != 0) thing += "&attempt=" + this.measures[i].attempts;
        console.log(thing);
      }
      //localStorage.removeItem("measures");
      return;
    }
    //localStorage.setItem("measures", JSON.stringify(this.measures));
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

  public resetMeasures() {
    this.measures = MEASURES;
    this.clearMeasures();
  }

  getMeasure(id: number): Observable<Measure> {
    // TODO: send the message _after_ fetching the hero
    this.messageService.add(`HeroService: fetched measure id=${id}`);
    this.populateMeasures();
    return of(this.measures.find(measure => measure.id === id));
  }

  getBlankMeasures(): Observable<Measure[]> {
    this.messageService.add('HeroService: fetched Measures');
    this.populateMeasures();

    return of(this.measures);
  }
}