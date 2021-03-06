import { AfterViewInit, Component } from '@angular/core';
import { Router, NavigationEnd } from '@angular/router';

@Component({
  selector: 'click-app',
  templateUrl: './home.component.html',
  styleUrls: ['./main.css']
})
export class HomeComponent implements AfterViewInit {
  private sub: any;

  videos:Array<String> = ["https://www.youtube.com/embed/B1ZJrWHJmV0", "https://www.youtube.com/embed/gmgVcmHm2YE", "https://www.youtube.com/embed/NT6J_suUQm4"];

  constructor(private _router : Router) {
  }
  ngAfterViewInit() {
    this.sub = this._router.events.subscribe(val => {
          if (val instanceof NavigationEnd) {
            (<any>window).twttr = (function (d, s, id) {
              let js: any, fjs = d.getElementsByTagName(s)[0],
                  t = (<any>window).twttr || {};
              if (d.getElementById(id)) return t;
              js = d.createElement(s);
              js.id = id;
              js.src = "https://platform.twitter.com/widgets.js";
              fjs.parentNode.insertBefore(js, fjs);

              t._e = [];
              t.ready = function (f: any) {
                  t._e.push(f);
              };

              return t;
            }(document, "script", "twitter-wjs"));

            if ((<any>window).twttr.ready())
              (<any>window).twttr.widgets.load();

          }
        });
  }

  ngOnDestroy() {
   this.sub.unsubscribe();
 }

}
