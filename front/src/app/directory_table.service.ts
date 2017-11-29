import { Injectable }              from '@angular/core';
import { Http, Response, URLSearchParams }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

export interface DirectoryTable {
  _id:string,
  social_reason: string,
  figure: string,
  federal_entity:string,
  representants: string,
  emails: string,
  place:string,
  street:string,
  network:string
 }

@Injectable()
export class organizationService {
  private orgUrl = 'http://clicksocial.mx/api/v0/directory';  // URL to web API
  params = new URLSearchParams();

  constructor(private http: Http) { }
  getData(): Observable<DirectoryTable[]> {
    this.params.set('filters', '0');
    return this.http.get(this.orgUrl, {search:this.params})
      .map(this.extractData)
      .catch(this.handleError);
  }

  getFilterData(f, i): Observable<DirectoryTable[]> {
    this.params.set('filters', '1');
    this.params.set('figure', f);
    this.params.set('issue', i);
    return this.http.get(this.orgUrl, {search:this.params})
      .map(this.extractData)
      .catch(this.handleError);
  }

  private extractData(res: Response) {
    let body = res.json();
    return body.directory || {};
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
