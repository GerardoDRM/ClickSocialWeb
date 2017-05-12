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
    "Alimentación",
    "Equidad de Género",
    "Profesionalización",
    "Investigación"
  ]
  group_filter = [
    "Población en general",
    "Productores",
    "Comunidades",
    "Poblaciones indígenas",
    "Personas con discapacidad",
    "Emprendedores (artesanos y productores)",
    "Niñas, Niños y Jóvenes",
    "Universidades, UNICEF",
    "Comunidades aledañas a sus cementeras",
    "Trabaja con OSC enfocadas en NNA y en temas de medio ambiente",
    "Jóvenes",
    "Personas con adicciones",
    "Personas con adicciones y población en general",
    "Personas en situación de calle",
    "Adultos mayores y menores en abandono, desamparo",
    "medio ambiente",
    "Comunidades donde laboran sus empleados",
    "Mujeres",
    "Personas con cáncer",
    "Indígenas",
    "Médicos"
  ]
  issue_filter = [
    "Nacional",
    "Yucatán",
    "Chihuahua",
    "Sonora",
    "Noroeste del País",
    "Ciudad de México",
    "Michoacán",
    "Internacional",
    "América Latina",
    "Morelos",
    "Cozumel",
    "Ciudad Juárez",
    "Cuernavaca",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Baja California",
    "Coahuila",
    "Estado de México",
    "Cd. Juárez, Chihuahua",
    "Veracruz",
    "Córdoba",
    "Matamoros",
    "Tecate ",
    "Jalisco",
    "Nuevo León",
    "Chihuhua"
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
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false}
  ];

  selectedIssue=[
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
    {"value": false},
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

    this.challengesService.getFilterData(newTypes, newGroup, newIssues).subscribe(
      response => this.organizations = response
    )

    var d = this.dialog.nativeElement;
    d.close();
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
  addImg(model) {
    var img = "";
    switch (model) {
      case "Desarrollo Integral":
        img = "../assets/imgs/integral.svg";
        break;
      case "Sociedad Incluyente":
        img = "../assets/imgs/incluyente.svg";
        break;
      case "Alimentación":
        img = "../assets/imgs/food.svg";
        break;
      case "Equidad de Género":
        img = "../assets/imgs/gender.svg";
        break;
      case "Profesionalización":
        img = "../assets/imgs/pro.svg";
        break;
      case "Investigación":
        img = "../assets/imgs/research.svg";
        break;
    }
   return img;
  }
  addColor(model) {
    var color = "";
    switch (model) {
      case "Desarrollo Integral":
        color = "#2962FF";
        break;
      case "Sociedad Incluyente":
        color = "#304FFE";
        break;
      case "Alimentación":
        color = "#FFC107";
        break;
      case "Equidad de Género":
        color = "#607D8B";
        break;
      case "Profesionalización":
        color = "#795548";
        break;
      case "Investigación":
        color = "#009688";
        break;
    }
   return color;
  }
}
