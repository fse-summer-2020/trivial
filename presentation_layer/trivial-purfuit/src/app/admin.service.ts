import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { QuestionApiResponse } from './game/model/question.model';
import { Category } from './game/model/category.model';
const httpOptionsPost = {
  headers: 
  new HttpHeaders({
      'Content-Type':  'application/json',
      'Access-Control-Request-Method': 'POST',
      'Access-Control-Allow-Origin': 'http://127.0.0.1:5000'
    })
};

const httpOptionsGet = {
  headers: 
  new HttpHeaders({
      'Content-Type':  'application/json',
      'Access-Control-Request-Method': 'GET',
      'Access-Control-Allow-Origin': 'http://127.0.0.1:5000'
    })
};
const url = "http://localhost:5000/"

@Injectable({
  providedIn: 'root'
})
export class AdminService {

  constructor(public http:HttpClient) { }

  public getQuestionPerCategory(category_id) {
    return this.http.get(url + 'utility/questions/' + category_id ,httpOptionsGet)
  }
  public getAllCategory() {
    return this.http.get(url + 'utility/all_categories' ,httpOptionsGet)
}
}
