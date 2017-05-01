import { Injectable }              from '@angular/core';
import { Http, Response, URLSearchParams }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

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
  img:string
 }

@Injectable()
export class organizationService {
  private orgUrl = 'http://localhost:5000/api/v0/organizations';  // URL to web API
  params = new URLSearchParams();

  constructor(private http: Http) { }
  getData(): Observable<Organization[]> {
    this.params.set('filters', '0');
    return this.http.get(this.orgUrl, {search:this.params})
      .map(this.extractData)
      .catch(this.handleError);
  }
  getFilterData(t, g, i): Observable<Organization[]> {
    this.params.set('filters', '1');
    this.params.set('type', t);
    this.params.set('group', g);
    this.params.set('issue', i);
    return this.http.get(this.orgUrl, {search:this.params})
      .map(this.extractData)
      .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    return body.organizations || {};
  }
  private handleError(error: Response | any) {
    // In a real world app, you might use a remote logging infrastructure
    let errMsg: string;
    if (error instanceof Response) {
      const body = error.json() || '';
      const err = body.error || JSON.stringify(body);
      errMsg = `${error.status} - ${error.statusText || ''} ${err}`;
    } else {
      errMsg = error.message ? error.message : error.toString();
    }
    console.error(errMsg);
    return Observable.throw(errMsg);
  }
}
