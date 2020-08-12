import { Component, Inject, OnInit } from '@angular/core';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { ConfigurationPageComponent } from '../configuration-page/configuration-page.component';
import { QuestionApiResponse } from '../game/model/question.model';
import { FormGroup, FormControl, Validators, ValidatorFn, AbstractControl } from '@angular/forms';

@Component({
  selector: 'app-edit-question-dialog',
  templateUrl: './edit-question-dialog.component.html',
  styleUrls: ['./edit-question-dialog.component.css']
})
export class EditQuestionDialogComponent implements OnInit{

  question: QuestionApiResponse;
  questionForm;
  constructor(
    public dialogRef: MatDialogRef<ConfigurationPageComponent>,
    @Inject(MAT_DIALOG_DATA) public data: QuestionApiResponse) {
      this.question = data
    }
  ngOnInit(): void {
    this.questionForm = new FormGroup({
      question: new FormControl(this.question.question, [
        Validators.required
      ]),
      possible_answer_0: new FormControl(this.question.possible_answers[0], Validators.required),
      possible_answer_1: new FormControl(this.question.possible_answers[1], Validators.required),
      possible_answer_2: new FormControl(this.question.possible_answers[2], Validators.required),
      possible_answer_3: new FormControl(this.question.possible_answers[3], Validators.required),
      correct_answer: new FormControl(this.question.correct_answer, [Validators.required, this.correctAnswerValidator(this.question.possible_answers)])
    });  }

    onPossibleAnswersChange(){
      console.log("change")
      this.questionForm.controls["correct_answer"].updateValueAndValidity();
    }
  onCancel(): void {
    this.dialogRef.close();
  }

  onSave(): void {
    if(this.questionForm.valid){
      this.dialogRef.close(this.question);
    }
  }
  trackByIdx(index: number, obj: any): any {
    return index;
  }

  correctAnswerValidator(list: string[]): ValidatorFn {
    return (control: AbstractControl): {[key: string]: any} | null => {
      return list.indexOf(control.value) > -1 ? null: {correctAnswer: {value: control.value}};
    };
  }
  get correct_answer(){
    return this.questionForm.get("correct_answer")
  }
}
