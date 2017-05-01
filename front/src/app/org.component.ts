import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './org.service';
import { OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

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
  img: string,
  contact: Array<string>,
 }

@Component({
  templateUrl: './org.component.html',
  styleUrls: ['./main.css'],
  providers: [organizationService]
})
export class OrgComponent implements AfterViewInit,OnInit, OnDestroy {
  organization: Organization = {
    _id:"",
    model:"",
    entity:"",
    social_group:"",
    federal_entity:"",
    geo_issue:"",
    web:"",
    email:"",
    type:"",
    img: "",
    contact: []
  };
  mode = 'Observable';
  private sub: any;
  id: string;

  constructor(private route: ActivatedRoute, private _elRef: ElementRef, private organizationService: organizationService) {
  }
  ngAfterViewInit() {
  }
  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = params['id'];
      this.getOrganizations(this.id);
    });
  }
  getOrganizations(id) {
    this.organizationService.getData(id).subscribe(
      response => this.organization = response
    )
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
