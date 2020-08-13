import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DeterminePlayerOrderComponent } from './determine-player-order.component';

describe('DeterminePlayerOrderComponent', () => {
  let component: DeterminePlayerOrderComponent;
  let fixture: ComponentFixture<DeterminePlayerOrderComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DeterminePlayerOrderComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DeterminePlayerOrderComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
