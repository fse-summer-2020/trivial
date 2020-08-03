import { Component, OnInit } from '@angular/core';
import { QuestionApiResponse } from '../../model/question.model';
import { Observable, Subscription } from 'rxjs';
import { HttpClient, HttpHeaders } from '@angular/common/http';


@Component({
  selector: 'app-question',
  templateUrl: './question.component.html',
  styleUrls: ['./question.component.css']
})
export class QuestionComponent implements OnInit {
  questionData : QuestionApiResponse;
  question: String;
  constructor(private httpClient: HttpClient) { }

  ngOnInit(): void {
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
