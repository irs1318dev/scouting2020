import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatchScoreCardComponent } from './match-score-card.component';

describe('MatchScoreCardComponent', () => {
  let component: MatchScoreCardComponent;
  let fixture: ComponentFixture<MatchScoreCardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MatchScoreCardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MatchScoreCardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
