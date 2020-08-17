import { Component, OnInit, Input } from "@angular/core";
import { Player } from "../../model/player.model";

@Component({
    selector: 'player-card',
    templateUrl: './playerCard.component.html',
    styleUrls: ['./playerCard.component.scss']
})
export class PlayerCardComponent implements OnInit {

    @Input()
    player: Player;

    constructor(){}

    ngOnInit(){}
}