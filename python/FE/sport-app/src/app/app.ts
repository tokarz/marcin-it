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

  constructor(private readonly apiService: ApiService){

  }
  async ngOnInit(): Promise<void> {
    this.data = await this.apiService.getData();
  }
}
