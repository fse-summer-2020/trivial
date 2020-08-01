import { Component, OnInit } from "@angular/core";
import { Router } from "@angular/router";

@Component({
    selector: 'intro-panel',
    templateUrl: './introPanel.component.html',
    styleUrls: ['./introPanel.component.css']
})
export class IntroPanelComponent implements OnInit {

    constructor(private router: Router) {}
    ngOnInit() {}
    navigateToGame() {
        console.log("insert navigation")
    }

    navigateToConfigurationMode() {
        console.log("insert navigation");
    }
}