import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './directory_table.service';

declare var dialogPolyfill: any;

export interface DirectoryTable {
  _id:string,
  federal_entity:string,
  municipio:string,
  place:string,
  street:string,
  inter_number:string,
  extern_number:string,
  cp:number,
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
