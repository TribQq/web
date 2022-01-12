import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class BbService {
  private url: String = 'http:://localhost:8000';
  constructor(private http: HttpClient) {}
  getBbs(): Observable<Object[]> {
    return this.http.get<Object[]>(this.url + '/api/bbs/');
}
}
