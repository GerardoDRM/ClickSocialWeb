import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './directory.service';

declare var dialogPolyfill: any;

export interface Organization {
  _id:string,
  model:string,
  entity:string,
  social_group:string,
  federal_entity:string,
  geo_issue:string,
  web:string,
  email:string,
  type:string,
  img: string;
 }

@Component({
  templateUrl: './directory.component.html',
  styleUrls: ['./main.css'],
  providers: [organizationService]
})
export class DirectoryComponent implements AfterViewInit {
  organizations: Organization[];
  mode = 'Observable';


  constructor(private _elRef: ElementRef, private challengesService: organizationService) {
  }
  ngAfterViewInit() {
  }
  ngOnInit() {
    this.getOrganizations();
  }
  getOrganizations() {
    this.challengesService.getData().subscribe(
      response => this.organizations = response
    )
  }
}
