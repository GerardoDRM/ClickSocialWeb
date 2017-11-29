import { Component } from '@angular/core';
import { ElementRef } from "@angular/core";
import { ViewChild } from "@angular/core";
import { AfterViewInit } from "@angular/core";
import { organizationService } from './directory_table.service';

declare var dialogPolyfill: any;

export interface DirectoryTable {
  _id: string,
  social_reason: string,
  figure: string,
  federal_entity: string,
  representants: string,
  emails: string,
  place: string,
  street: string,
  network: string
}

@Component({
  templateUrl: './directory_table.component.html',
  styleUrls: ['./main.css'],
  providers: [organizationService]
})
export class DirectoryTableComponent {
  @ViewChild('dialog') dialog: ElementRef;
  organizations: DirectoryTable[];
  mode = 'Observable';
  data = '';


  figure_filter = [
    "Institución de Asistencia Privada",
    "Asociación Civil",
    "Otra",
    "Sociedad Civil",
    "Asociación de Beneficiencia Privada",
    "Institución de Beneficiencia Privada (IBP)"
  ];

  issue_filter = [
    "Querétaro",
    "Tamaulipas",
    "Distrito Federal",
    "Estado de México",
    "Sinaloa",
    "Coahuila",
    "Jalisco",
    "Campeche",
    "Oaxaca",
    "Nuevo León",
    "Sonora",
    "San Luis Potosí",
    "Guanajuato",
    "Puebla",
    "Chiapas",
    "Tabasco",
    "Veracruz",
    "Guerrero",
    "Hidalgo",
    "Yucatán",
    "Michoacán",
    "Morelos",
    "Tlaxcala",
    "Baja California",
    "Aguascalientes",
    "Chihuahua",
    "Quintana Roo",
    "Durango",
    "Colima",
    "Zacatecas",
    "Baja California Sur"
  ]

  selectedFigure = [
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false }
  ];

  selectedIssue = [
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false },
    { "value": false }
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
    let newFigures = "";
    let newIssues = "";
    for(var i=0; i < this.selectedFigure.length; i++) {
      if (this.selectedFigure[i].value) {
        newFigures+=this.figure_filter[i] + ',';
      }
    }
    newFigures = newFigures.slice(0, -1);

    for(var i=0; i < this.selectedIssue.length; i++) {
      if (this.selectedIssue[i].value) {
        newIssues+=this.issue_filter[i] + ',';
      }
    }
    newIssues = newIssues.slice(0, -1);

    this.challengesService.getFilterData(newFigures, newIssues).subscribe(
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
}
