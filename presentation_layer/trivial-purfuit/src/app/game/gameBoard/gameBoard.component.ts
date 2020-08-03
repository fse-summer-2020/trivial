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
    answerTriviaForm: FormGroup;
    setCategoryForm: FormGroup;
    sessionId: string
    gameStateResponse: Observable<any>;
    isRollDieState: boolean = false;
    isMoveDirectionState: boolean = false;
    isAnswerTriviaState: boolean = false;
    isSetCategoryState: boolean = false;
    currentPlayer: Player;
    currentRound: number;
    playerList: Player[];
    nextAvailableSquares: number[][]
    movesLeft: number;
    direction: string;
    currentQuestion: string;
    possibleAnswers: string[];
    answer: string;
    category: string;
    available_categories: any;

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
                this.isAnswerTriviaState = false;
                break;
            }
            case "MOVE_DIRECTION": {
                this.isMoveDirectionState = true;
                this.isRollDieState = false;
                this.createMoveDirectionForm();
                break;
            }
            case "ANSWER_TRIVIA": {
                this.isMoveDirectionState = false;
                this.isSetCategoryState = false;
                this.isAnswerTriviaState = true;
                this.createAnswerTriviaForm();
                break;
            }
            case "POLL_CATEGORY_ALL": {
                this.isMoveDirectionState = false;
                this.isSetCategoryState = true;
                this.createSetCategoryForm();
                break;
            }
            case "POLL_CATEGORY_CURRENT": {
                this.isMoveDirectionState = false;
                this.isSetCategoryState = true;
                this.createSetCategoryForm();
                break;
            }
        }
    }

    rollDie() {
        this.gameStateResponse = this.service.getRollDie(this.sessionId);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.nextAvailableSquares = data.state.available_next_squares;
            this.currentRound = data.state.current_round;
            this.currentPlayer = data.state.current_player;
            this.playerList = data.state.players;
            this.movesLeft = data.state.moves_left;
            this.updateCurrentState(data.state.current_state);
        });
    }

    answerTriviaQuestion() {
        this.answer = this.answerTriviaForm.get(
            'trivia'
        ).value;
        console.log(this.answer);
        this.gameStateResponse = this.service.answerTrivia(this.sessionId, this.answer);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.currentRound = data.state.current_round;
            this.currentPlayer = data.state.current_player;
            this.playerList = data.state.players;
            this.movesLeft = data.state.moves_left;
            this.updateCurrentState(data.state.current_state);        
        })
    }

    setCategory() {
        this.category = this.setCategoryForm.get(
            'category'
        ).value;
        this.gameStateResponse = this.service.setCategory(this.sessionId, this.category);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.currentRound = data.state.current_round;
            this.currentPlayer = data.state.current_player;
            this.playerList = data.state.players;
            this.movesLeft = data.state.moves_left;
            this.updateCurrentState(data.state.current_state);        
        })
    }

    createAnswerTriviaForm(): void {
        this.answerTriviaForm = this.formBuilder.group({
            trivia: ''
        })
    }
    
    createMoveDirectionForm(): void {
      this.moveDirectionForm = this.formBuilder.group({
          direction: ''
      })
    }

    createSetCategoryForm(): void {
        this.setCategoryForm = this.formBuilder.group({
            category: ''
        })
    }

    moveDirection() {
        this.direction = this.moveDirectionForm.get(
            'direction'
        ).value;
        console.log(this.direction);
        this.gameStateResponse = this.service.moveDirection(this.sessionId, this.direction);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.nextAvailableSquares = data.state.available_next_squares;
            this.currentRound = data.state.current_round;
            this.currentPlayer = data.state.current_player;
            this.playerList = data.state.players;
            this.movesLeft = data.state.moves_left;
            if(data.state.current_trivia_question) {
                this.currentQuestion = data.state.current_trivia_question.question;
                this.possibleAnswers = data.state.current_trivia_question.possible_answers;
            }
            console.log(this.possibleAnswers);
            this.updateCurrentState(data.state.current_state);
        });
    }
    
    ngOnInit() {
        this.service.getAllCategory().toPromise().then((data: any)=>{
            this.available_categories = data.categories
        })
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