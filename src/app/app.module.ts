import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule, Routes, Router } from '@angular/router';

import { AppComponent } from './app.component';
import { SuccesCaseComponent } from './succescase.component'
import { SuccesCasesComponent } from './succescases.component'
import { HomeComponent } from './home.component'
import { ContestComponent } from './contest.component'
import { AnnouncesComponent } from './announces.component'

const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'cases', component: SuccesCasesComponent },
  { path: 'case', component: SuccesCaseComponent },
  { path: 'contests', component: ContestComponent },
  { path: 'announces', component: AnnouncesComponent }

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
    HomeComponent,
    ContestComponent,
    AnnouncesComponent
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(router: Router) {
    console.log('Routes: ', JSON.stringify(router.config, undefined, 2));
  }
}
