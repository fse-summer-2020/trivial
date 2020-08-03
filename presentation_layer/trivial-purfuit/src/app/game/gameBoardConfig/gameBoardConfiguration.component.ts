import { Component, OnInit } from "@angular/core";
import { Router, ActivatedRoute } from "@angular/router";

@Component({
    selector: 'board-configuration',
    templateUrl: './gameBoardConfiguration.component.html',
    styleUrls: ['./gameBoardConfiguration.component.css']
})
export class GameBoardConfigurationComponent implements OnInit {
    constructor(
        private router: Router,
        private route: ActivatedRoute
    ){}
    ngOnInit() {}

    navigateToGame() {
        this.router.navigate(['../game'], { relativeTo: this.route } );
    }
}