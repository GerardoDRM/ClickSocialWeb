import { Component, OnInit } from '@angular/core';
import { StoryService } from './successcases.service';

export interface Story {
  _id: string;
  title: string;
  description: string;
  img: string;
  creation_date: number;
}

@Component({
  selector: 'app-succescases',
  templateUrl: './succescases.component.html',
  styleUrls: ['./main.css'],
  providers: [StoryService]
})

export class SuccesCasesComponent implements OnInit {
  stories: Story[];
  mode = 'Observable';

  constructor(private storyService: StoryService) { }
  ngOnInit() {
    this.getStories();
  }
  getStories() {
    this.storyService.getStories().subscribe(
      response => this.stories = response
    )
  }
}
