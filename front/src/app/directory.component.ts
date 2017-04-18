import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";

declare var dialogPolyfill: any;


@Component({
  templateUrl: './directory.component.html',
  styleUrls: ['./main.css']
})
export class DirectoryComponent implements AfterViewInit {
  constructor(private _elRef: ElementRef) {
  }
  ngAfterViewInit() {

  }
}
