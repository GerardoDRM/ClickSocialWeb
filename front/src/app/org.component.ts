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
  contact: string,
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
    contact: ""
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
  addWallpaper(model) {
    var img = "";
    switch (model) {
      case "Desarrollo Integral":
        img = "../assets/imgs/road_big.jpg";
        break;
      case "Sociedad Incluyente":
        img = "../assets/imgs/nodes.jpeg";
        break;
      case "Alimentación":
        img = "../assets/imgs/alim.jpeg";
        break;
      case "Equidad de Género":
        img = "../assets/imgs/gender.jpg";
        break;
      case "Profesionalización":
        img = "../assets/imgs/prof.jpg";
        break;
      case "Investigación":
        img = "../assets/imgs/research.jpg";
        break;
    }
   return img;
  }
  addDesc(model) {
    var text = "";
    switch (model) {
      case "Desarrollo Integral":
        text = "Decripcion para desarrollo integral";
        break;
      case "Sociedad Incluyente":
        text = "Decripcion para Incluyente";
        break;
      case "Alimentación":
        text = "Decripcion para Alimentación";
        break;
      case "Equidad de Género":
        text = "Decripcion para Género";
        break;
      case "Profesionalización":
        text = "Decripcion para Profesionalización";
        break;
      case "Investigación":
        text = "Decripcion para Investigación";
        break;
    }
   return text;
  }
}
