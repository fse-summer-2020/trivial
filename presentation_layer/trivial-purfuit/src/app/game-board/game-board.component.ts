import { Component, OnInit, Input, AfterViewChecked, OnChanges } from '@angular/core';
import { Category } from '../game/model/category.model';
import { Player } from '../game/model/player.model';

@Component({
  selector: 'game-board',
  templateUrl: './game-board.component.html',
  styleUrls: ['./game-board.component.css']
})
export class GameBoardComponent implements AfterViewChecked {

  ROWS = 9
  COLS = 9
  board : any[][]
  @Input()
  categories : Category[]
  @Input()
  players : Player[]
  constructor() { }



  ngAfterViewChecked(): void {
    this.board=[[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null],[null,null,null,null,null,null,null,null,null]]
    this.board[0][4] = {type:"HQ", color: this.categories[0].color}
    this.board[4][0] = {type:"HQ", color: this.categories[1].color}
    this.board[8][4] = {type:"HQ", color: this.categories[3].color}
    this.board[4][8] = {type:"HQ", color: this.categories[2].color}

        this.board[0][2] = {type:"RA", color: "white"}
        this.board[0][6] = {type:"RA", color: "white"}
        this.board[2][0] = {type:"RA", color: "white"}
        this.board[2][8] = {type:"RA", color: "white"}
        this.board[6][8] = {type:"RA", color: "white"}
        this.board[6][0] = {type:"RA", color: "white"}
        this.board[8][2] = {type:"RA", color: "white"}
        this.board[8][6] = {type:"RA", color: "white"}

        this.board[4][4] = {type:"H", color: "purple"}

        
        this.board[0][0] = {type:"C", color: this.categories[0].color}
        this.board[0][1] = {type:"C", color: this.categories[1].color}
        this.board[0][3] = {type:"C", color: this.categories[3].color}
        this.board[0][5] = {type:"C", color: this.categories[3].color}
        this.board[0][7] = {type:"C", color: this.categories[1].color}
        this.board[0][8] = {type:"C", color: this.categories[2].color}

        this.board[1][0] =  {type:"C", color: this.categories[3].color}
        this.board[1][4] =  {type:"C", color: this.categories[3].color}
        this.board[1][8] =  {type:"C", color: this.categories[0].color}
        this.board[2][4] =  {type:"C", color: this.categories[1].color}
        this.board[3][0] = {type:"C", color: this.categories[2].color}
        this.board[3][4] = {type:"C", color: this.categories[0].color}
        this.board[3][8] = {type:"C", color: this.categories[1].color}

        this.board[4][1] = {type:"C", color: this.categories[2].color}
        this.board[4][2] = {type:"C", color: this.categories[3].color}
        this.board[4][3] = {type:"C", color: this.categories[1].color}
        this.board[4][5] = {type:"C", color: this.categories[2].color}
        this.board[4][6] = {type:"C", color: this.categories[0].color}
        this.board[4][7] = {type:"C", color: this.categories[1].color}

        this.board[5][0] = {type:"C", color: this.categories[2].color}
        this.board[5][4] = {type:"C", color: this.categories[3].color}
        this.board[5][8] = {type:"C", color: this.categories[1].color}

        this.board[6][4] = {type:"C", color: this.categories[2].color}

        this.board[7][0] = {type:"C", color: this.categories[3].color}
        this.board[7][4] = {type:"C", color: this.categories[0].color}
        this.board[7][8] = {type:"C", color: this.categories[0].color}

        this.board[8][0] = {type:"C", color: this.categories[1].color}
        this.board[8][1] = {type:"C", color: this.categories[2].color}
        this.board[8][3] = {type:"C", color: this.categories[0].color}
        this.board[8][5] = {type:"C", color: this.categories[0].color}
        this.board[8][7] = {type:"C", color: this.categories[2].color}
        this.board[8][8] = {type:"C", color: this.categories[3].color}
  }
  
  getColor(rId, cId){
    return this.board[rId][cId]["color"]
  }

  getTokensOnLocation(rId, cId){
    let filtered = this.players.filter((player)=>{
      return JSON.stringify(player.location) === JSON.stringify([rId, cId])
    })
    return filtered
  }


}
