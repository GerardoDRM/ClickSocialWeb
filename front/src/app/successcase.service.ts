import { Injectable }              from '@angular/core';
import { Http, Response }          from '@angular/http';
import { Observable } from 'rxjs/Observable';
import 'rxjs/add/operator/catch';
import 'rxjs/add/operator/map';

export interface Contact {
  name:string;
  email:string;
}

export interface Story {
    _id: string;
    title: string;
    description: string;
    img: string;
    creation_date: number;
    web:string;
    contact: Contact;
 }


@Injectable()
export class StoryService {
  private storiesUrl = 'http://localhost:5000/api/v0/stories';  // URL to web API
  constructor(private http: Http) { }
  getStories(id): Observable<Story> {
    return this.http.get(this.storiesUrl + "/" + id)
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
