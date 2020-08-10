import { Component, Inject } from '@angular/core';
import {MatDialogRef, MAT_DIALOG_DATA} from '@angular/material/dialog';
import { ConfigurationPageComponent } from '../configuration-page/configuration-page.component';
import { QuestionApiResponse } from '../game/model/question.model';

@Component({
  selector: 'app-edit-question-dialog',
  templateUrl: './edit-question-dialog.component.html',
  styleUrls: ['./edit-question-dialog.component.css']
})
export class EditQuestionDialogComponent {

  question: QuestionApiResponse;

  constructor(
    public dialogRef: MatDialogRef<ConfigurationPageComponent>,
    @Inject(MAT_DIALOG_DATA) public data: QuestionApiResponse) {
      this.question = data
    }

  onCancel(): void {
    this.dialogRef.close();
  }
  trackByIdx(index: number, obj: any): any {
    return index;
  }
}
