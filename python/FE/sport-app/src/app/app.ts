import { Component } from '@angular/core';
import { OnInit } from '../../node_modules/@angular/core/index';
import { ApiService } from './fetching/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.scss'
})
export class AppComponent implements OnInit {
  protected title = 'sport-app';
  public data:any='';
  public clubs:any[]=[];
  public players:any[]=[];
  public coach:any[]=[];

  constructor(private readonly apiService: ApiService){

  }
  ngOnInit(): void {
    this.apiService.getData().subscribe((data:any) => {
      this.data = data;
      this.clubs = data.data;
    })
  }

  public loadPlayers(klubId:string){
    this.apiService.getPlayers(klubId).subscribe((data:any) => {
      this.data = data;
      this.players = data.data;
    })
  }
  public loadCoach(klubId:string){
    this.apiService.getCoach(klubId).subscribe((data:any) => {
      this.data = data;
      this.coach = data.data;
    })
  }
}
