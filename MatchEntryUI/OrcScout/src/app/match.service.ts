import { Injectable, HostListener } from '@angular/core';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { RedVBlue } from './models/redVblue';
import { catchError, map, tap } from 'rxjs/operators';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})

export class MatchService {

  constructor(private http: HttpClient, private messageService: MessageService) { }
  
  private matchTeamsUrl = 'http://localhost:8080/match/matchteams';  // URL to web api

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

  getMatch(matchNumber: string): Observable<RedVBlue> {
    var url = `${this.matchTeamsUrl}`;
    if (matchNumber !== null && matchNumber !== '')
    {
      url += `/${matchNumber}`
    }
    return this.http.get<RedVBlue>(url)
      .pipe(
        tap(_ => this.log('fetched matches')),
        catchError(this.handleError<RedVBlue>('getHeroes'))
      );
  }
}
