import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Player } from '../game/model/player.model';

@Component({
  selector: 'app-end-game-page',
  templateUrl: './end-game-page.component.html',
  styleUrls: ['./end-game-page.component.css']
})
export class EndGamePageComponent implements OnInit {

  players : Player[]
  constructor(
    private route: ActivatedRoute) { 
      this.route.params.subscribe((params: Params) => this.players = JSON.parse(params['players']));
    }

  ngOnInit(): void {
  }

  winningPlayers(){
   return  this.players.filter((player)=>{
      console.log(player.collected_wedges.length == 4)
      return player.collected_wedges.length == 4
    })
  }
}
