import { Component, OnInit, ChangeDetectorRef } from "@angular/core";
import { GameBoardService } from "../service/gameBoard.service";
import { Player } from "../model/player.model";
import { Observable } from 'rxjs';
import { FormGroup, FormBuilder } from '@angular/forms'
import { Category } from '../model/category.model';
import { Router, ActivatedRoute } from '@angular/router';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
    selector: 'app-game-board',
    templateUrl: './gameBoardManager.component.html',
    styleUrls: ['./gameBoardManager.component.css']
})
export class GameBoardManagerComponent implements OnInit {

    moveDirectionForm: FormGroup;
    answerTriviaForm: FormGroup;
    setCategoryForm: FormGroup;
    sessionId: string
    gameStateResponse: Observable<any>;
    isRollDieState: boolean = false;
    isMoveDirectionState: boolean = false;
    isAnswerTriviaState: boolean = false;
    isSetCategoryCurrentState: boolean = false;
    isSetCategoryAllState: boolean = false;
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
    available_categories: Category[];
    isCorrectAnswer: boolean;
    isIncorrectAnswer: boolean;

    constructor(
        private service: GameBoardService,
        private formBuilder: FormBuilder,
        private router: Router,
        private route: ActivatedRoute,
        private snackBar: MatSnackBar
    ) {}

    players: Player[] = []

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
                this.isSetCategoryCurrentState = false;
                this.isSetCategoryAllState = false;
                this.isAnswerTriviaState = true;
                this.createAnswerTriviaForm();
                break;
            }
            case "POLL_CATEGORY_ALL": {
                this.isMoveDirectionState = false;
                this.isSetCategoryAllState = true;
                this.createSetCategoryForm();
                break;
            }
            case "POLL_CATEGORY_CURRENT": {
                this.isMoveDirectionState = false;
                this.isSetCategoryCurrentState = true;
                this.createSetCategoryForm();
                break;
            }
            case "END_GAME": {
                this.router.navigate(['end-game', {players: JSON.stringify(this.playerList)}], { relativeTo: this.route });
            }
        }
    }

    rollDie() {
        this.gameStateResponse = this.service.getRollDie(this.sessionId);
        this.gameStateResponse.subscribe(data => {
            console.log(data);
            this.isCorrectAnswer = false;
            this.isIncorrectAnswer = false;
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
            if(this.currentPlayer.color === data.state.current_player.color) {
                this.openSnackBar("Correct Answer!", "Close");            }
            else{
                this.openSnackBar("Incorrect Answer", "Close");
            }
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
            this.currentQuestion = data.state.current_trivia_question.question;
            this.possibleAnswers = data.state.current_trivia_question.possible_answers;
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

    openSnackBar(message: string, action: string) {
        this.snackBar.open(message, action, {
            duration: 2000,
        });
    }
    
    ngOnInit() {
        this.players = this.service.sortedPlayers;
        this.service.getAllCategory().toPromise().then((categories: Category[])=>{
            this.available_categories = categories
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