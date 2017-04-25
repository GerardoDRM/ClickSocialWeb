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
    likes: 0
  };
  mode = 'Observable';

  constructor(private route: ActivatedRoute, private challengesService: ChallengeService) { }
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
    this.challengesService.getChallenge(id).subscribe(
     response => this.challenge = response

    )
  }
  ngOnDestroy() {
    this.sub.unsubscribe();
  }

}
