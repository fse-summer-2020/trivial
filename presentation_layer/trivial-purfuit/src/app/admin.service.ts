import { Injectable } from '@angular/core';
import { HttpHeaders, HttpClient } from '@angular/common/http';
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
  
  public getAllCategory(){
    return this.http.get(url + 'utility/all_categories' ,httpOptionsGet)
}
}
