import { Component, OnInit, ChangeDetectorRef } from "@angular/core";
import { GameBoardService } from "../service/gameBoard.service";
import { Player } from "../model/player.model";
import { Observable } from 'rxjs';
import { FormGroup, FormBuilder } from '@angular/forms'

@Component({
    selector: 'game-board',
    templateUrl: './gameBoard.component.html',
    styleUrls: ['./gameBoard.component.css']
})
export class GameBoardComponent implements OnInit {

    moveDirectionForm: FormGroup;
    sessionId: string
    gameStateResponse: Observable<any>;
    isRollDieState: boolean = false;
    isMoveDirectionState: boolean = false;
    currentPlayer: Player;
    currentRound: number;
    playerList: Player[];
    nextAvailableSquares: number[][]
    movesLeft: number;

    constructor(
        private service: GameBoardService,
        private formBuilder: FormBuilder
    ) {}

    players: Player[] = [
    {
        name: 'Ben Franklin',
        color: 'red'
    },
    {
        name: 'Alexander Hamilton',
        color: 'white'
    },
    {
        name: 'Thomas Jefferson',
        color: 'blue'
    },
    {
        name: 'John Hancock',
        color: 'green' 
    }
    ];

    updateCurrentState(state: string) {
        switch(state) {
            case "ROLL_DIE": {
                this.isRollDieState = true;
                this.isMoveDirectionState = false;
                break;
            }
            case "MOVE_DIRECTION": {
                this.isMoveDirectionState = true;
                this.isRollDieState = false;
                this.createMoveDirectionForm();
                break;
            }
        }
    }

    rollDie() {
        this.gameStateResponse = this.service.getRollDie(this.sessionId);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.updateCurrentState(data.state.current_state);
            this.nextAvailableSquares = data.state.available_next_squares;
            console.log(this.nextAvailableSquares);
            this.movesLeft = data.state.moves_left;
        });
    }
    
    createMoveDirectionForm(): void {
      this.moveDirectionForm = this.formBuilder.group({
          direction: ''
      })
    }
    
    ngOnInit() {
        this.gameStateResponse = this.service.createGame(this.players);
        this.gameStateResponse.subscribe(data => {
            this.sessionId = data.session_id
            this.currentRound = data.state.current_round;
            this.currentPlayer = data.state.current_player;
            this.playerList = data.state.players;
            this.movesLeft = data.state.moves_left;
            this.updateCurrentState(data.state.current_state);
        });
    }
}