import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PhaseEndgameComponent } from './phase-finish.component';

describe('PhaseEndgameComponent', () => {
  let component: PhaseEndgameComponent;
  let fixture: ComponentFixture<PhaseEndgameComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PhaseEndgameComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PhaseEndgameComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
