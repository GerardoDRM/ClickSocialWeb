import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './directory_table.service';

declare var dialogPolyfill: any;

export interface DirectoryTable {
  _id:string,
  social_reason: string,
  figure: string,
  federal_entity:string,
  representants: string,
  emails: string,
  place:string,
  street:string,
  network:string
}

@Component({
  templateUrl: './directory_table.component.html',
  styleUrls: ['./main.css'],
  providers: [organizationService]
})
export class DirectoryTableComponent {
  organizations: DirectoryTable[];
  mode = 'Observable';

  constructor(private _elRef: ElementRef, private challengesService: organizationService) {
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
