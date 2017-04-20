import { Component, OnInit, ElementRef, ViewChild } from '@angular/core';
import { AfterViewInit } from "@angular/core";
declare var dialogPolyfill: any;
import { ChallengeService } from './announces.service';

export interface Challenge {
    _id: string;
    title: string;
    description: string;
    img: string;
    creation_date: number;
    likes: number;
 }

@Component({
  templateUrl: './announces.component.html',
  styleUrls: ['./main.css'],
  providers: [ChallengeService]

})
export class AnnouncesComponent implements AfterViewInit, OnInit {
  @ViewChild('dialog') dialog: ElementRef;
  challenges: Challenge[];
  mode = 'Observable';

  constructor(private _elRef: ElementRef, private challengesService: ChallengeService) {
  }
  dateTransform(number) {
    var t = new Date( number * 1000 );
    return t.getDate() + "/" + (t.getMonth()+1) + "/" + t.getFullYear();
  }
  ngOnInit() {
    this.getChallenges();
  }
  getChallenges() {
    this.challengesService.getChallenges().subscribe(
      response => this.challenges = response
    )
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
