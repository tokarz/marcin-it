// src/app/api.service.ts
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class ApiService {
  private http = inject(HttpClient);
  private apiUrl = 'http://localhost:8000/kluby';

  getData() {
    return this.http.get(this.apiUrl);
  }

  getPlayers(klub_id:string) {
    return this.http.get(`http://localhost:8000/clubplayers?klub_id=${klub_id}`);
  }
  getCoach(klub_id:string) {
    return this.http.get(`http://localhost:8000/clubtrener?klub_id=${klub_id}`);
  }
}