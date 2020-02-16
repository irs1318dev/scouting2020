import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { PhaseTeleopComponent } from './phase-teleop.component';

describe('PhaseTeleopComponent', () => {
  let component: PhaseTeleopComponent;
  let fixture: ComponentFixture<PhaseTeleopComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ PhaseTeleopComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(PhaseTeleopComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
