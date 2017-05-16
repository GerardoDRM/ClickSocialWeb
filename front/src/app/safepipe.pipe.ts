import { Pipe, PipeTransform } from '@angular/core';
import { DomSanitizer} from '@angular/platform-browser';


// Tell Angular2 we're creating a Pipe with TypeScript decorators
@Pipe({
  name: 'safe'
})
export class SafePipe implements PipeTransform {
  constructor(private sanitizer: DomSanitizer) {}
  // Transform is the new "return function(value, args)" in Angular 1.x
  transform(value) {
    // ES6 array destructuring
    if (value !== undefined) {
      return this.sanitizer.bypassSecurityTrustResourceUrl(value);
    }
  }

}
