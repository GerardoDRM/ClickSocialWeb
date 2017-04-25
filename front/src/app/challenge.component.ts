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
    authors:Author[];
    address:Address;
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
  challenge: Challenge[];
  mode = 'Observable';

  constructor(private route: ActivatedRoute, private challengesService: ChallengeService) { }
  ngOnInit() {
    this.sub = this.route.params.subscribe(params => {
      this.id = params['id'];
      this.getChallenge(this.id);
    });
  }
  getChallenge(id) {
    this.challengesService.getChallenge(id).subscribe(
    //  response => this.challenge = response

    )
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
