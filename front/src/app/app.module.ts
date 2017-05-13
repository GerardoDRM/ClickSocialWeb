import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule, JsonpModule } from '@angular/http';
import { RouterModule, Routes, Router } from '@angular/router';

import { AppComponent } from './app.component';
import { SuccesCaseComponent } from './succescase.component'
import { SuccesCasesComponent } from './succescases.component'
import { HomeComponent } from './home.component'
import { ContestComponent } from './contest.component'
import { AnnouncesComponent } from './announces.component'
import { DirectoryComponent } from './directory.component'
import { DirectoryTableComponent } from './directory_table.component'
import { ChallengeComponent } from './challenge.component'
import { OrgComponent } from './org.component'
import { FilterPipe } from './filtersearch.pipe'
const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'cases', component: SuccesCasesComponent },
  { path: 'case/:id', component: SuccesCaseComponent },
  { path: 'contests', component: ContestComponent },
  { path: 'announces', component: AnnouncesComponent },
  { path: 'directory', component: DirectoryComponent },
  { path: 'challenge/:id', component: ChallengeComponent },
  { path: 'org/:id', component: OrgComponent },
  { path: 'directory_table', component: DirectoryTableComponent },


];

@NgModule({
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    JsonpModule,
    RouterModule.forRoot(appRoutes)
  ],
  declarations: [
    AppComponent,
    SuccesCasesComponent,
    SuccesCaseComponent,
    HomeComponent,
    ContestComponent,
    AnnouncesComponent,
    DirectoryComponent,
    ChallengeComponent,
    DirectoryTableComponent,
    OrgComponent,
    FilterPipe
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule {
  constructor(router: Router) {
    console.log('Routes: ', JSON.stringify(router.config, undefined, 2));
  }
}
