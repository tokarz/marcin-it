import { Component, OnInit, signal, computed } from '@angular/core';

import { ApiService } from './fetching/api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.scss',
})
export class AppComponent implements OnInit {
  protected title = 'sport-app';
  public data: any = '';
  public clubs: any[] = [];
  public players: any[] = [];
  public coach = signal('');
  public printCoach = computed(() => {
    const currentCoach = this.coach();
    if (currentCoach && currentCoach[0]) {
      if (currentCoach[0].length == 2) {
        return `${currentCoach[0][1]} ${currentCoach[0][0]}`;
      } else {
        return currentCoach;
      }
    } else {
      return '';
    }
  });

  public tSportTeams = signal('Sport Teams');

  public selectedKlub = signal('');
  public bgImage = signal('en');

  constructor(private readonly apiService: ApiService) {}
  ngOnInit(): void {
    this.apiService.getData().subscribe((data: any) => {
      this.data = data;
      this.clubs = data.data;
    });
  }

  public loadPlayers(klubId: string) {
    this.selectedKlub.set(klubId);
    this.apiService.getPlayers(klubId).subscribe((data: any) => {
      this.data = data;
      this.players = data.data;
    });
  }
  public loadCoach(klubId: string) {
    this.apiService.getCoach(klubId).subscribe((data: any) => {
      this.data = data;
      this.coach.set(data.data);
    });
  }

  public toggleLang() {
    if (this.bgImage() === 'pl') {
      this.bgImage.set('en');
    } else {
      this.bgImage.set('pl');
    }
  }
}
