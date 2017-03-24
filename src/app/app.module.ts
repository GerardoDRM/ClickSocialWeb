import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes, Router } from '@angular/router';

import { AppComponent } from './app.component';
import { SuccesCaseComponent } from './succescase.component'
import { SuccesCasesComponent } from './succescases.component'
import { HomeComponent } from './home.component'

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'cases', component: SuccesCasesComponent },
  { path: 'case', component: SuccesCaseComponent },
];


@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(appRoutes)
  ],
  declarations: [
    AppComponent,
    SuccesCasesComponent,
    SuccesCaseComponent,
    HomeComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(router: Router) {
    console.log('Routes: ', JSON.stringify(router.config, undefined, 2));
  }
}
