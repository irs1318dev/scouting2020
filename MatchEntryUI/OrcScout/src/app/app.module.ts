import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'; // <-- NgModel lives here
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule }    from '@angular/common/http';

import { AppComponent } from './app.component';
import { HeroesComponent } from './heroes/heroes.component';
import { HeroDetailComponent } from './hero-detail/hero-detail.component';
import { MessagesComponent } from './messages/messages.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { MatchComponent } from './match/match.component';
import { MeasureComponent } from './measure/measure.component';
import { MatchScoreCardComponent } from './match-score-card/match-score-card.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { PhaseAutoComponent } from './phase-auto/phase-auto.component';

import { MatFormFieldModule, MatInputModule, MatButtonModule, MatSlideToggleModule, MatSliderModule, 
  MatSidenavModule, MatToolbarModule, MatCardModule, MatSelectModule, MatStepperModule, MatListModule } 
  from '@angular/material';

@NgModule({
  declarations: [
    AppComponent,
    HeroesComponent,
    HeroDetailComponent,
    MessagesComponent,
    DashboardComponent,
    MatchComponent,
    MeasureComponent,
    MatchScoreCardComponent,
    PhaseAutoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MatSidenavModule,
    MatToolbarModule,
    MatButtonModule,
    MatSlideToggleModule,
    MatFormFieldModule,
    MatInputModule,
    MatCardModule,
    MatSelectModule,
    MatStepperModule,
    MatListModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }