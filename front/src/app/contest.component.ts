import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";

declare var dialogPolyfill: any;


@Component({
  templateUrl: './contest.component.html',
  styleUrls: ['./main.css']
})
export class ContestComponent implements AfterViewInit {
  @ViewChild('dialog') dialog: ElementRef;
  constructor(private _elRef: ElementRef) {
  }
  ngAfterViewInit() {
    var d = this.dialog.nativeElement;
    if (! d.showModal) {
      dialogPolyfill.registerDialog(d);
    }
  }
  openDialog() {
    var d = this.dialog.nativeElement;
    d.showModal();
  }
  closeDialog() {
    var d = this.dialog.nativeElement;
    d.close();
  }

}
