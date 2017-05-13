import { Pipe, PipeTransform } from '@angular/core';

export interface DirectoryTable {
  _id: string,
  social_reason: string,
  figure: string,
  federal_entity: string,
  representants: string,
  emails: string,
  place: string,
  street: string,
  network: string
}

// Tell Angular2 we're creating a Pipe with TypeScript decorators
@Pipe({
  name: 'filterdata'
})
export class FilterData implements PipeTransform {

  // Transform is the new "return function(value, args)" in Angular 1.x
  transform(value, args?): DirectoryTable {
    // ES6 array destructuring
    if (value !== undefined) {
      let data = args;
      if (data != "") {
        return value.filter(o => {
          if (new RegExp(data).test(o.federal_entity) || new RegExp(data).test(o.social_reason)) {
            return  o;
          }
        });
      }
      else {
       return value.filter(o => {
         return o;
       });
     }
    }
  }

}
