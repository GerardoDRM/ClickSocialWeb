import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './directory.service';

declare var dialogPolyfill: any;

export interface Organization {
  _id: string,
  model: string,
  entity: string,
  social_group: string,
  federal_entity: string,
  geo_issue: string,
  web: string,
  email: string,
  type: string,
  img: string;
}

@Component({
  templateUrl: './directory.component.html',
  styleUrls: ['./main.css'],
  providers: [organizationService]
})
export class DirectoryComponent implements AfterViewInit {
  @ViewChild('dialog') dialog: ElementRef;
  organizations: Organization[];
  mode = 'Observable';
  type_filter = [
    "Desarrollo Integral",
    "Sociedad Incluyente",
    "Alimentacion",
    "Equidad de genero",
    "Profesionalizacion",
    "Investigacion"
  ]
  group_filter = [
    "Población en general",
    "Productores",
    "Comunidades"
  ]
  issue_filter = [
    "Nacional",
    "Estatal",
    "Municipal",
    "Delegacion"
  ]

  selectedTypes=[
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false}
  ];

  selectedGroup=[
    {"value": false},
    {"value": false},
    {"value": false}
  ];

  selectedIssue=[
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false}
  ];


  constructor(private _elRef: ElementRef, private challengesService: organizationService) {
  }
  ngAfterViewInit() {
    var d = this.dialog.nativeElement;
    if (!d.showModal) {
      dialogPolyfill.registerDialog(d);
    }
  }
  searchData() {
    let newTypes = "";
    let newGroup = "";
    let newIssues = "";
    for(var i=0; i < this.selectedTypes.length; i++) {
      if (this.selectedTypes[i].value) {
        newTypes+=this.type_filter[i] + ',';
      }
    }
    newTypes = newTypes.slice(0, -1);
    for(var i=0; i < this.selectedGroup.length; i++) {
      if (this.selectedGroup[i].value) {
        newGroup+=this.group_filter[i] + ',';
      }
    }
    newGroup = newGroup.slice(0, -1);
    for(var i=0; i < this.selectedIssue.length; i++) {
      if (this.selectedIssue[i].value) {
        newIssues+=this.issue_filter[i] + ',';
      }
    }
    newIssues = newIssues.slice(0, -1);

    console.log(newGroup, newIssues);
    // this.challengesService.getFilterData(newTypes, newGroup, newIssues).subscribe(
    //   response => this.organizations = response
    // )
  }
  openDialog() {
    var d = this.dialog.nativeElement;
    d.showModal();
  }
  closeDialog() {
    var d = this.dialog.nativeElement;
    d.close();
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
