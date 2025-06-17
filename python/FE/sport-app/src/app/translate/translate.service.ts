import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class TranslateService {
  public translations: { [key: string]: { [key: string]: string } } = {
    pl: {
      players: 'Zawodnicy',
      teams: 'Drużyny',
      portfolio: 'Portfolio',
      coach: 'Trener',
      selectClub: 'Wybierz Klub!',
    },
    en: {
        players: 'Players',
        teams: 'Teams',
        portfolio: 'Portfolio',
        coach: 'Coach',
        selectClub: 'Choose club!',
    },
  };
}
