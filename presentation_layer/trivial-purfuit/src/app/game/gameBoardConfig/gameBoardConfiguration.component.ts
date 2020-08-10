import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute } from "@angular/router";
import { GameBoardService } from "../service/gameBoard.service";
import { Player } from "../model/player.model";
import { FormBuilder, FormGroup } from "@angular/forms";

@Component({
    selector: 'board-configuration',
    templateUrl: './gameBoardConfiguration.component.html',
    styleUrls: ['./gameBoardConfiguration.component.css']
})
export class GameBoardConfigurationComponent implements OnInit {

    players: Player[] =  [];
    playerForm: FormGroup;

    constructor(
        private router: Router,
        private route: ActivatedRoute, 
        private service: GameBoardService,
        private formBuilder: FormBuilder
    ){}

    ngOnInit() {
        this.createPlayerForm();
    }

    createPlayerForm(): void {
        this.playerForm = this.formBuilder.group({
            firstName: '',
            lastName: '',
            color: ''
        })
    }

    submitPlayer() {
      const player = {
            name: this.playerForm.get('firstName').value + ' ' + 
            this.playerForm.get('lastName').value,
            color: this.playerForm.get('color').value
        }
        console.log(player);
        this.players.push(player);
        console.log(this.players);
        this.service.addPlayer(player);
        console.log(this.service.players);
        this.createPlayerForm();

    }

    navigateToGame() {
        this.service.determinePlayerOrder();
        this.router.navigate(['../game'], { relativeTo: this.route } );
    }
}