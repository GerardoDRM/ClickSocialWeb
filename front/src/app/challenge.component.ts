import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ChallengeService } from './challenge.service';

export interface Address {
  state:string;
  city:string;
}
export interface Author {
  name:string;
  email:string;
}
export interface Comment {
  author:string;
  comment:string;
}
export interface Challenge {
    _id: string;
    title: string;
    description: string;
    challenge:string;
    img: string;
    creation_date: number;
    likes: number;
    authors: Array<Author>;
    address: Array<Address>;
 }

@Component({
  selector: 'app-succescase',
  templateUrl: './challenge.component.html',
  styleUrls: ['./main.css'],
  providers: [ChallengeService]
})
export class ChallengeComponent implements OnInit, OnDestroy {
  private sub: any;
  id: string;
  challenge: Challenge = {
    _id: "",
    title: "",
    description: "",
    challenge: "",
    img: "",
    creation_date: 0,
    likes: 0,
    authors: [],
    address: []
  };
  comments: Comment[];

  author:string;
  comment:string;
  mode = 'Observable';

  constructor(private route: ActivatedRoute, private challengesService: ChallengeService) { }
  ngOnInit() {
    this.author = "";
    this.comment = "";

    this.sub = this.route.params.subscribe(params => {
      this.id = params['id'];
      this.getData(this.id);
    });
  }
  dateTransform(number) {
    var t = new Date( number * 1000 );
    return t.getDate() + "/" + (t.getMonth()+1) + "/" + t.getFullYear();
  }
  addCommet() {
    // Send comment
    this.challengesService.sendComment(this.author, this.comment, this.id);
    // Get new comments list
    this.challengesService.getComments(this.id).subscribe(
      response => this.comments = response
    );
    this.author = "";
    this.comment = "";
  }
  getData(id) {
    this.challengesService.getChallenge(id).subscribe(
     response => this.challenge = response
    )
    this.challengesService.getComments(id).subscribe(
      response => this.comments = response
    );
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
