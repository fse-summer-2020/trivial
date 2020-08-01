import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';

const httpOptions = {
    headers: 
    new HttpHeaders({
        'Content-Type':  'application/json',
        'Access-Control-Request-Method': 'GET',
        'Access-Control-Allow-Origin': 'http://127.0.0.1:5000'
      })
  };
const url = "http://localhost:5000/logic/"

@Injectable()
export class GameBoardService{


    
    constructor(public http:HttpClient){}

    public moveDirection(session_id: string, direction: string){
        return this.http.post(url + 'move_direction', {
            session_id: session_id,
            direction: direction
        },httpOptions)
    }

    public createGame(players: object){
        return this.http.post(url + 'create_game', {
            players: players
        },httpOptions)
    }

    public setCategory(session_id: string, category: string){
        return this.http.post(url + 'set_category', {
            session_id: session_id,
            category: category
        },httpOptions)
    }

    public answerTrivia(session_id: string, answer: string){
        return this.http.post(url + 'answer_trivia', {
            session_id: session_id,
            answer: answer
        },httpOptions)
    }

    public getRollDie(session_id: string){
        return this.http.post(url + 'roll_die',{
            session_id: session_id
        },httpOptions)
    }
}
