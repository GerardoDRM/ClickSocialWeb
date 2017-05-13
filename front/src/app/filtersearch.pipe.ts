import {Pipe} from '@angular/core';

// Tell Angular2 we're creating a Pipe with TypeScript decorators
@Pipe({
  name: 'FilterPipe'
})
export class FilterPipe {

  // Transform is the new "return function(value, args)" in Angular 1.x
  transform(value, args?) {
    // ES6 array destructuring
    let [data] = args;
    return value.filter(o => {
      return o.federal_entity == data || o.social_reason == data;
    });
  }

}
