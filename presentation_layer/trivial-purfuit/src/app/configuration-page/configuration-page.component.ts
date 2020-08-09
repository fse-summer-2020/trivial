import { Component, OnInit, Inject } from '@angular/core';
import { AdminService } from '../admin.service';
import {MatDialog} from '@angular/material/dialog';
import { EditQuestionDialogComponent } from '../edit-question-dialog/edit-question-dialog.component';
import { Category } from '../game/model/category.model';
import { QuestionApiResponse } from '../game/model/question.model';
import * as uuid from 'uuid';
import { ActivatedRoute, Router } from '@angular/router';



@Component({
  selector: 'app-configuration-page',
  templateUrl: './configuration-page.component.html',
  styleUrls: ['./configuration-page.component.css']
})
export class ConfigurationPageComponent implements OnInit {

  questions : any = {}
  categories : any = []
  css_colors = [
    "AliceBlue",
    "AntiqueWhite",
    "Aqua",
    "Aquamarine",
    "Azure",
    "Beige",
    "Bisque",
    "Black",
    "BlanchedAlmond",
    "Blue",
    "BlueViolet",
    "Brown",
    "BurlyWood",
    "CadetBlue",
    "Chartreuse",
    "Chocolate",
    "Coral",
    "CornflowerBlue",
    "Cornsilk",
    "Crimson",
    "Cyan",
    "DarkBlue",
    "DarkCyan",
    "DarkGoldenRod",
    "DarkGray",
    "DarkGrey",
    "DarkGreen",
    "DarkKhaki",
    "DarkMagenta",
    "DarkOliveGreen",
    "DarkOrange",
    "DarkOrchid",
    "DarkRed",
    "DarkSalmon",
    "DarkSeaGreen",
    "DarkSlateBlue",
    "DarkSlateGray",
    "DarkSlateGrey",
    "DarkTurquoise",
    "DarkViolet",
    "DeepPink",
    "DeepSkyBlue",
    "DimGray",
    "DimGrey",
    "DodgerBlue",
    "FireBrick",
    "FloralWhite",
    "ForestGreen",
    "Fuchsia",
    "Gainsboro",
    "GhostWhite",
    "Gold",
    "GoldenRod",
    "Gray",
    "Grey",
    "Green",
    "GreenYellow",
    "HoneyDew",
    "HotPink",
    "IndianRed",
    "Indigo",
    "Ivory",
    "Khaki",
    "Lavender",
    "LavenderBlush",
    "LawnGreen",
    "LemonChiffon",
    "LightBlue",
    "LightCoral",
    "LightCyan",
    "LightGoldenRodYellow",
    "LightGray",
    "LightGrey",
    "LightGreen",
    "LightPink",
    "LightSalmon",
    "LightSeaGreen",
    "LightSkyBlue",
    "LightSlateGray",
    "LightSlateGrey",
    "LightSteelBlue",
    "LightYellow",
    "Lime",
    "LimeGreen",
    "Linen",
    "Magenta",
    "Maroon",
    "MediumAquaMarine",
    "MediumBlue",
    "MediumOrchid",
    "MediumPurple",
    "MediumSeaGreen",
    "MediumSlateBlue",
    "MediumSpringGreen",
    "MediumTurquoise",
    "MediumVioletRed",
    "MidnightBlue",
    "MintCream",
    "MistyRose",
    "Moccasin",
    "NavajoWhite",
    "Navy",
    "OldLace",
    "Olive",
    "OliveDrab",
    "Orange",
    "OrangeRed",
    "Orchid",
    "PaleGoldenRod",
    "PaleGreen",
    "PaleTurquoise",
    "PaleVioletRed",
    "PapayaWhip",
    "PeachPuff",
    "Peru",
    "Pink",
    "Plum",
    "PowderBlue",
    "Purple",
    "RebeccaPurple",
    "Red",
    "RosyBrown",
    "RoyalBlue",
    "SaddleBrown",
    "Salmon",
    "SandyBrown",
    "SeaGreen",
    "SeaShell",
    "Sienna",
    "Silver",
    "SkyBlue",
    "SlateBlue",
    "SlateGray",
    "SlateGrey",
    "Snow",
    "SpringGreen",
    "SteelBlue",
    "Tan",
    "Teal",
    "Thistle",
    "Tomato",
    "Turquoise",
    "Violet",
    "Wheat",
    "White",
    "WhiteSmoke",
    "Yellow",
    "YellowGreen",
  ];
  

  constructor(private adminService: AdminService, public dialog: MatDialog, private router: Router,
    private route: ActivatedRoute) { }

  ngOnInit(): void {
    this.adminService.getAllCategory().toPromise().then((res : any) =>{
      res.categories.forEach((category: Category) => {
        this.categories.push(category)
        let category_id = category._id.$oid
        this.questions[category_id] = {}
        this.adminService.getQuestionPerCategory(category_id).toPromise().then((res:any)=>{
          res.questions.forEach((question: QuestionApiResponse) => {
            this.questions[category_id][question._id.$oid] = question
          });
          
        })
      });
    })
  }
  getQuestions(category_id): Array<any>{
    return this.questions[category_id]
  }

  selectQuestion(question){
    const dialogRef = this.dialog.open(EditQuestionDialogComponent, {
      width: '500px',
      data: question
    });

    dialogRef.afterClosed().subscribe(question => {
      if(question == undefined || question.question == "" || question.correct_answer == "" || question.possible_answers.indexOf("") > -1 || question.possible_answers.indexOf(question.correct_answer) < 0){
        return
      }
      const question_id = question._id.$oid
      const category_id = question.category_id.$oid
      this.questions[category_id][question_id] = question
    });
  }

  addQuestion(category:Category){
    const dialogRef = this.dialog.open(EditQuestionDialogComponent, {
      width: '500px',
      data: {_id: {$oid:""}, question:"", possible_answers:["","","",""], correct_answer:"", category_id : category._id}
    });

    dialogRef.afterClosed().subscribe((question:QuestionApiResponse) => {

      if(question == undefined || question.question == "" || question.correct_answer == "" || question.possible_answers.indexOf("") > -1 || question.possible_answers.indexOf(question.correct_answer) < 0){
        return
      }
      const question_id = "new_question_" + uuid.v4()
      const category_id = question.category_id.$oid
      question._id.$oid = question_id
      this.questions[category_id][question_id] = question
    });
  }

  removeQuestion(question){
    console.log(question)
    const question_id = question._id.$oid
    const category_id = question.category_id.$oid
    delete this.questions[category_id][question_id]
  }

  onCancel(){
    this.router.navigate([''], { relativeTo: this.route} );

  }

  onSave(){
    this.router.navigate([''], { relativeTo: this.route} );

  }
}