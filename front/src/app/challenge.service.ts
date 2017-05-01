import { Injectable }              from '@angular/core';
import { Http, Response }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';


export interface Address {
  state:string;
  city:string;
}
export interface Author {
  name:string;
  email:string;
}
export interface Commnet {
  user:string;
  name:string;
  content:string;
}
export interface Challenge {
    _id: string;
    title: string;
    description: string;
    challenge:string;
    img: string;
    creation_date: number;
    likes: number;
    comments: Comment[];
    authors: Array<Author>;
    address: Array<Address>;
 }

@Injectable()
export class ChallengeService {
  private challengesUrl = 'http://localhost:5000/api/v0/challenges';  // URL to web API
  constructor(private http: Http) { }
  getChallenge(id): Observable<Challenge> {
    return this.http.get(this.challengesUrl+"/"+id)
      .map(this.extractData)
      .catch(this.handleError);
  }
  private extractData(res: Response) {
    let body = res.json();
    console.log(body);
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
