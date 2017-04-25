import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { StoryService } from './successcase.service';


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
 }


@Component({
  selector: 'app-succescase',
  templateUrl: './succescase.component.html',
  styleUrls: ['./main.css'],
  providers: [StoryService]
})
export class SuccesCaseComponent implements OnInit, OnDestroy {
  private sub: any;
  id: string;
  story: Story = {
    _id: "",
    title: "",
    description: "",
    img: "",
    creation_date: 0,
    web: ""
  };
  mode = 'Observable';

  constructor(private route: ActivatedRoute, private storyService: StoryService) { }
  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = params['id'];
      this.getData(this.id);
    });
  }
  dateTransform(number) {
    var t = new Date( number * 1000 );
    return t.getDate() + "/" + (t.getMonth()+1) + "/" + t.getFullYear();
  }
  getData(id) {
    this.storyService.getStories(id).subscribe(
      response => this.story = response
    )
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }
}
