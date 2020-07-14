import { Component } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { QuestionApiResponse } from './model/question.model';
import { Observable, Subscription } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'trivial-purfuit';
  questionData : QuestionApiResponse;
  question: String;

  constructor(private httpClient: HttpClient) {}

  ngOnInit() {
    this.getQuestion().subscribe(data => {
      this.questionData = data;
      this.question = data.question;
      console.log(this.questionData);
      console.log(this.question);
    })
  }

  getQuestion(): Observable<QuestionApiResponse> {
    return this.httpClient.get<QuestionApiResponse>('http://127.0.0.1:5000/question/random_question', {
      headers: new HttpHeaders({
        Accept: 'application/json;v=4',
        'Content-Type': 'application/json;v=4',
        'Access-Control-Request-Method': 'GET',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5000'
      })
    });
  }

}
