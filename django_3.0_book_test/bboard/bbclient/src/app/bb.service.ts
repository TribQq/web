import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable, window } from 'rxjs';
import { of } from 'rxjs'; 
import { catchError } from 'rxjs';
import { HttpHeaders } from '@angular/common/http';




@Injectable({
  providedIn: 'root'
})
export class BbService {
  private url: String = 'http:://localhost:8000';
  constructor(private http: HttpClient) {}
  getBbs(): Observable<Object[]> {
    return this.http.get<Object[]>(this.url + '/api/bbs/');
  }
  handleError() {
    return (error: any): Observable<Object>=> {
      window.alert(error.message);
      return of(null);
    }
  }
  //  674 должно вызывать окно с ошибкой. но иде ругается на несоотвествие типов. хотя я вроде их не присаиваю.. или?)
  addComment(bb: String, author: String, password:String, 
    content:String): Observable<Object> {
      const comment = {'bb': bb, 'author': author, 'content': content};
      const options = {'header': new HttpHeaders(
        {'Content-type': 'application/json', 
      'Authorization': 'Basic ' + window.btoa(author + ':' + password)})};
    return this.http.post<Object>(this.url + '/api/bbs/' + bb + '/comments', comment,
    options).pipe(catchError(this.handleError()));
    }
  getComments(pk: Number): Observable<Object[]>{
    return this.http.get<Object[]>(this.url + '/api/bbs/' + pk + '/comments/');
  }
}
