import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { GameState } from '../model/gameState.model';
import { Observable } from 'rxjs';
import { Player } from '../model/player.model';

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

@Injectable()
export class GameBoardService{
    
    constructor(public http:HttpClient){}

    public moveDirection(session_id: string, direction: string){
        return this.http.post(url + 'logic/move_direction', {
            session_id: session_id,
            direction: direction
        },httpOptionsPost)
    }

    public createGame (players: object) {
        return this.http.post(url + 'logic/create_game', {
            players: players
        },httpOptionsPost)
    }

    public setCategory(session_id: string, category_id: string){
        return this.http.post(url + 'logic/set_category', {
            session_id: session_id,
            category_id: category_id
        },httpOptionsPost)
    }

    public answerTrivia(session_id: string, answer: string){
        return this.http.post(url + 'logic/answer_trivia', {
            session_id: session_id,
            answer: answer
        },httpOptionsPost)
    }

    public getRollDie(session_id: string){
        return this.http.post(url + 'logic/roll_die',{
            session_id: session_id
        },httpOptionsPost)
    }

    public getAllCategory(){
        return this.http.get(url + 'category/all' ,httpOptionsGet)
    }
}
