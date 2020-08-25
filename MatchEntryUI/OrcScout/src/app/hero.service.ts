import { Injectable, HostListener } from '@angular/core';
import { Measure } from './match';
import { MEASURES } from './mock-heroes';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { RedVBlue, ScoreRecord } from './models/redVblue';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Match } from './match';
import { MatchScoreCardComponent } from './match-score-card/match-score-card.component';
import { Component, OnInit, Input } from '@angular/core';
import { phases, PhasesLabel } from './domain-tables/phases';

@Injectable({
  providedIn: 'root',
})

export class HeroService {

  measures: Measure[];
  constructor(private http: HttpClient, private messageService: MessageService) { }
  
  private matchTeamsUrl = 'http://localhost:8080/match/matchteams';  // URL to web api
  private scoreUrl = 'http://localhost:8080/match/score';  // URL to web api
  private updateScoreUrl = 'http://localhost:8080/match/updatescore';  // URL to web api

  
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
    let matchedMeasure = this.measures.find(m => m.task_name === record.task && PhasesLabel.get(m.phase) === record.phase);
    if (matchedMeasure)
    {
      matchedMeasure.successes = record.successes;
      matchedMeasure.attempts = record.attempts;
    }
  }

  // TODO: Arushi, this is where we can post to the server the score.  
  public postScore(team: string, match: string): void
  {
    for (let meas of this.measures)
    {
      var urlString = `${this.updateScoreUrl}/${match}/${team}/${meas.task_name}/${phases[meas.phase]}/0/${this.getAttempts(meas.attempts)}/${meas.successes}`;     
      
      this.http.post(urlString, "")
      .pipe(
        tap(_ => this.log('update score')),
        catchError(this.handleError('getHeroes')))
      .subscribe();
    }// use the urlString above to call using a get (we're going to change this but for not it works) the server.
    // use the method below as a simple example of how to do this.  BUT you won't need a catch, and you'll want (again for now) a get<any>(). 
    // You want a get<any> because our server doesn't return valid json when it's succeeding.  A typical rest api would use something like 200, 201, or another valid return
    // status to indicate that it got a message back and worked.  It also might return a url which you can use to go get the new valid resource. 
    // we don't do that right now so we'll just call it with any, so it doesn't fail when we get data back from the server and it says, umm... I can't deserialize "hi".
    // If you do get an exception even with any here, then we need to change the python file, the simplest way to do this would be to create some fake return object in python.
    // and return that.

    // - in python - 
    // returnVal = {}
    // return returnVal
  }

  // as weird as it seems we post to the DB in the same manner that we get.  We can probably use
  // query parameters but this works too. 

  getAttempts(attempts: number | boolean): number{
    if(typeof attempts === "number"){
        return attempts;
    }
    
    if(typeof attempts === "boolean"){
      if(attempts){
        return 1;
      }
      return 0;
    }
  }


  getScore(team: string, match: string): Observable<ScoreRecord[]> {
      let results = this.http.get<ScoreRecord[]>(`${this.scoreUrl}/${team}/${match}`)
        .pipe(
          tap(_ => this.log('fetched score')),
          catchError(this.handleError<ScoreRecord[]>('getHeroes'))
        );
        
      return results;
  }

  // TODO: we should probably change this from ID to display name, or another lookup.
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