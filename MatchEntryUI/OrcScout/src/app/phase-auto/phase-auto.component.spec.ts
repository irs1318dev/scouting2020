import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PhaseAutoComponent } from './phase-auto.component';

describe('PhaseAutoComponent', () => {
  let component: PhaseAutoComponent;
  let fixture: ComponentFixture<PhaseAutoComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PhaseAutoComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PhaseAutoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
