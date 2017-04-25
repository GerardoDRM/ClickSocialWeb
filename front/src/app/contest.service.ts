import {Injectable} from '@angular/core';
import { Http, Response }  from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

export interface Convocations {


  title: string;
  type: string;
  web: string;
  _id: string;
  description: string;
  img: string;
  addresses: Address[];
 authors: Authors[];
 creation_date: number;
 model: string[];


}

export interface Address {

  city:string;
  state:string;
  street:string;

}

export interface Authors {
  email:string;
  name:string;
}


@Injectable()

export class ConvocationService {
  private ConvocationsUrl = 'http://localhost:5000/api/v0/convocations';  // URL to web API
  constructor(private http: Http) { }
  getConvocations(): Observable<Convocations[]> {
    return this.http.get(this.ConvocationsUrl)
      .map(this.extractData)
      .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    return body.convocations || {};
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
