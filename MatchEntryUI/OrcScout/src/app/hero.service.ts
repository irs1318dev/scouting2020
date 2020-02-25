import { Injectable, HostListener } from '@angular/core';
import { Hero } from './hero';
import { Measure } from './match';
import { HEROES, MEASURES } from './mock-heroes';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { RedVBlue, ScoreRecord } from './models/redVblue';
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
  
  private matchTeamsUrl = 'http://localhost:8080/match/matchteams';  // URL to web api
  private scoreUrl = 'http://localhost:8080/match/score';  // URL to web api

  
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
    return this.http.get<RedVBlue>(this.matchTeamsUrl)
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

  // This method saves the measures to local storage it is not meant to be used to 
  // save measures to the api.  We'll need to build that out.  
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

  public startMatch(team: string, match: string): Observable<Measure[]> {
    this.measures = MEASURES;
    this.getScore(team, match).subscribe(c => c.forEach(rec => this.assignMeasure(rec)));
    return of(this.measures);
  }

  assignMeasure(record: ScoreRecord){
    let matchedMeasure = this.measures.find(m => m.task_name === record.task);
    if (matchedMeasure)
    {
      matchedMeasure.successes = record.successes;
      matchedMeasure.attempts = record.attempts;
    }
  }

  getScore(team: string, match: string): Observable<ScoreRecord[]> {
      return this.http.get<ScoreRecord[]>(`${this.scoreUrl}/${team}/${match}`)
        .pipe(
          tap(_ => this.log('fetched score')),
          catchError(this.handleError<ScoreRecord[]>('getHeroes'))
        );
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