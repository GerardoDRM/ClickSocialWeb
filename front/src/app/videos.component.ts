import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';


@Component({
  selector: 'app-videos',
  templateUrl: './videos.component.html',
  styleUrls: ['./main.css']
})
export class VideosComponent implements OnInit, OnDestroy {
  private sub: any;
  conferences:Array<String> = ["https://www.youtube.com/embed/B1ZJrWHJmV0", "https://www.youtube.com/embed/gmgVcmHm2YE", "https://www.youtube.com/embed/NT6J_suUQm4"];
  capsules: Array<String> = ["https://www.youtube.com/embed/qhjTEnIrGMs", "https://www.youtube.com/embed/Tfyni7ah1xM", "https://www.youtube.com/embed/17QXGqU20k0"];
  mode = 'Observable';

  constructor(private route: ActivatedRoute) { }

  ngOnInit() {

  }

  ngOnDestroy() {

  }
}
