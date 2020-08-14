import { Component, OnInit, Input } from '@angular/core';
import { Category } from '../game/model/category.model';
import { Player } from '../game/model/player.model';


@Component({
  selector: 'token',
  templateUrl: './token.component.html',
  styleUrls: ['./token.component.css']
})
export class TokenComponent implements OnInit {

  @Input()
  player: Player;
  
  constructor() { }

  ngOnInit(): void {
  }

  getCategoryColor(index){
    if(this.player.collected_wedges.length >= index +1){
      return this.player.collected_wedges[index].color
    }else{
      return "#e6e6e6";
    }
  }
}
