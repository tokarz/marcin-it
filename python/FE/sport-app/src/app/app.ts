import {
  Component,
  OnInit,
  OnDestroy,
  signal,
  computed,
  ElementRef,
  WritableSignal,
} from '@angular/core';

import { ApiService } from './fetching/api.service';
import { TranslateService } from './translate/translate.service';
import { PortfolioComponent } from './portfolio/portfolio.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.html',
  styleUrl: './app.scss',
  imports: [PortfolioComponent],
})
export class AppComponent implements OnInit, OnDestroy {
  private clickListener = (event: MouseEvent) => this.onGlobalClick(event);

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

  public selectedPlayer = signal({} as any);

  public currentLanguage = signal('pl');
  public currentTranslations: WritableSignal<{ [key: string]: string }> =
    signal({});

  public currentDictionary = computed(() => {
    const currentLanguage = this.currentLanguage();

    return this.translationService.translations[currentLanguage];
  });

  public tSportTeams = computed(() => {
    const translations = this.currentDictionary();
    return translations['teams'];
  });
  public tPlayers = computed(() => {
    const translations = this.currentDictionary();
    return translations['players'];
  });
  public tPortfolio = computed(() => {
    const translations = this.currentDictionary();
    return translations['portfolio'];
  });
  public tCoach = computed(() => {
    const translations = this.currentDictionary();
    return translations['coach'];
  });
  public tSelectClub = computed(() => {
    const translations = this.currentDictionary();
    return translations['selectClub'];
  });

  public selectedKlub = signal('');

  constructor(
    private elRef: ElementRef,
    private readonly apiService: ApiService,
    private readonly translationService: TranslateService
  ) {}
  ngOnInit(): void {
    document.addEventListener('click', this.clickListener, true);
    this.apiService.getData().subscribe((data: any) => {
      this.data = data;
      this.clubs = data.data;
    });
    this.currentTranslations.set(
      this.translationService.translations[this.currentLanguage()]
    );
  }

  ngOnDestroy() {
    document.removeEventListener('click', this.clickListener, true);
  }

  public selectedPlayerData = computed(() => {
    const selectedPlayer = this.selectedPlayer();

    return {
      name: selectedPlayer,
      age: '22',
      nationality: 'polish',
    };
  });

  public resetSelection() {
    this.selectedKlub.set('');
    this.players = [];
    this.coach.set('');
  }

  public selectPlayer(player: any) {
    this.selectedPlayer.set(player);
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
    if (this.currentLanguage() === 'pl') {
      this.currentLanguage.set('en');
    } else {
      this.currentLanguage.set('pl');
    }
  }

  private onGlobalClick(event: MouseEvent) {
    const clickedInside = this.elRef.nativeElement.querySelector('.sport-app-wrapper').contains(event.target);
    if (!clickedInside) {
      this.resetSelection();
    }
  }
}
