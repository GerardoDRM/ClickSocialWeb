import { Component, OnInit } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { ConvocationService } from './contest.service';


declare var dialogPolyfill: any;


export interface Convocations {


  title: string;
  type: string;
  web: string;
  _id: string;
  description: string;
  img: string;
  addresses: Address[];
  authors: Authors[];
  creation_date: number;
  model: string[];


}

export interface Address {

  city: string;
  state: string;
  street: string;

}

export interface Authors {
  email: string;
  name: string;
}


export interface Dialog {
  title: string;
  description: string;
}


@Component({
  templateUrl: './contest.component.html',
  styleUrls: ['./main.css'],
  providers: [ConvocationService]
})
export class ContestComponent implements OnInit, AfterViewInit {

  convocations: Convocations[];
  mode = 'Observable';
  dialogC: Dialog = {title:"", description: ""};


  @ViewChild('dialog') dialog: ElementRef;

  constructor(private _elRef: ElementRef, private convocationsService: ConvocationService) {


  }

  ngOnInit() {
    this.getConvocations();
  }
  getConvocations() {
    this.convocationsService.getConvocations().subscribe(
      response => this.convocations = response
      )
  }
  dateTransform(number) {
    var t = new Date( number * 1000 );
    return t.getDate() + "/" + (t.getMonth()+1) + "/" + t.getFullYear();
  }
  ngAfterViewInit() {
    var d = this.dialog.nativeElement;
    if (!d.showModal) {
      dialogPolyfill.registerDialog(d);
    }
  }
  openDialog(convocation) {
    var d = this.dialog.nativeElement;
    d.showModal();
    this.dialogC = convocation;

    console.log(this.dialogC);
  }
  closeDialog() {
    var d = this.dialog.nativeElement;
    d.close();
  }

}
