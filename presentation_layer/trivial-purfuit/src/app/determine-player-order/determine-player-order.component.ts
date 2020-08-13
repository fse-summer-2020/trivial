import { Component, OnInit } from '@angular/core';
import { GameBoardService } from '../game/service/gameBoard.service';
import { ActivatedRoute, Router } from '@angular/router';
import { Player } from '../game/model/player.model';
import { AdminService } from '../admin.service';

@Component({
  selector: 'app-determine-player-order',
  templateUrl: './determine-player-order.component.html',
  styleUrls: ['./determine-player-order.component.css']
})
export class DeterminePlayerOrderComponent implements OnInit {

  playerOrderMap : Map<Player, number>;
  constructor(
    private router: Router,
    private route: ActivatedRoute, 
    private service: GameBoardService, 
    private adminService: AdminService) { }

  ngOnInit(): void {
    this.playerOrderMap = new Map()
    this.service.players.forEach((player:Player)=>{
      this.playerOrderMap.set(player, undefined)
    })
  }
  
  rollDie(player){
    this.adminService.rollDie().toPromise().then((res:any)=>{
        this.playerOrderMap.set(player,res.dice[0].value)
    })
  }

  navigateToGame() {
    let sortedMap = new Map([...this.playerOrderMap.entries()].sort((a, b) => a[1] - b[1]));
    let sortedPlayers = []
    sortedMap.forEach((value, player) => {
        sortedPlayers.push(player);
    });
    this.service.sortedPlayers = sortedPlayers
    this.router.navigate(['../game'], { relativeTo: this.route } );

  }
  isPlayerOrderDetermined(){
    return !Array.from(this.playerOrderMap.values()).includes(undefined)
  }
}
