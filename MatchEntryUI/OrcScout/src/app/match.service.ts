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

  getRedVBlue(matchNumber: string): Observable<RedVBlue> {
    return this.http.get<RedVBlue>(`${this.heroesUrl}/${matchNumber}`)
      .pipe(
        tap(_ => this.log('fetched heroes')),
        catchError(this.handleError<RedVBlue>('getHeroes'))
      );
  }
}
