import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute } from "@angular/router";
import { GameBoardService } from "../service/gameBoard.service";
import { Player } from "../model/player.model";
import { FormBuilder, FormGroup } from "@angular/forms";
import { Category } from '../model/category.model';

@Component({
    selector: 'board-configuration',
    templateUrl: './gameBoardConfiguration.component.html',
    styleUrls: ['./gameBoardConfiguration.component.css']
})
export class GameBoardConfigurationComponent implements OnInit {

    players: Player[] =  [];
    playerForm: FormGroup;
    displayError = false;
    availableColors = new Set<String>();

    constructor(
        private router: Router,
        private route: ActivatedRoute, 
        private service: GameBoardService,
        private formBuilder: FormBuilder
    ){}

    ngOnInit() {
        this.service.getAllCategory().toPromise().then((categories: Category[])=>{
            categories.forEach((category: Category) => {
                this.availableColors.add(category.color)
            });
        })
        this.createPlayerForm();
    }

    createPlayerForm(): void {
        this.playerForm = this.formBuilder.group({
            uname: null,
            color: null
        })
    }

    submitPlayer() {
        if (this.playerForm.get('uname').value
        && this.playerForm.get('color').value) {
        const player = {
                name: this.playerForm.get('uname').value,
                color: this.playerForm.get('color').value
            }
            this.availableColors.delete(player.color)
            console.log(player);
            this.players.push(player);
            console.log(this.players);
            this.service.addPlayer(player);
            console.log(this.service.players);
            this.createPlayerForm();
            this.displayError = false;
        }
        else {
            this.displayError = true;
        }
    }

    navigateToPlayerOrder() {
        this.router.navigate(['../player-order'], { relativeTo: this.route } );
    }
}