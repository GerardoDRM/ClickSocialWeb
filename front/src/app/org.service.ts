import { Injectable }              from '@angular/core';
import { Http, Response }          from '@angular/http';
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
  img:string,
  contact: Array<string>

 }

@Injectable()
export class organizationService {
  private orgUrl = 'http://clicksocial.mx/api/v0/organizations';  // URL to web API
  constructor(private http: Http) { }
  getData(id): Observable<Organization> {
    return this.http.get(this.orgUrl+"/"+id)
      .map(this.extractData)
      .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    return body || {};
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
