import { Component, AfterViewInit, ElementRef } from '@angular/core';

@Component({
  selector: 'click-app',
  templateUrl: './app.component.html',
  styleUrls: ['./main.css']
})
export class AppComponent implements AfterViewInit{

  constructor(private elRef:ElementRef) {
  }
  ngAfterViewInit() {
    var el = this.elRef.nativeElement.querySelector('.mdl-layout__drawer-button');
    console.log(el);
  }
}
