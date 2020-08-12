import { Component, OnInit } from "@angular/core";
import { ActivatedRoute, Router } from "@angular/router";

@Component({
    selector: 'intro-panel',
    templateUrl: './introPanel.component.html',
    styleUrls: ['./introPanel.component.css']
})
export class IntroPanelComponent implements OnInit {

    constructor(private router: Router,
        private route: ActivatedRoute) {}
    ngOnInit() {}
    navigateToGame() {
        this.router.navigate(['game-config'], { relativeTo: this.route} );
    }

    navigateToConfigurationMode() {
        this.router.navigate(['config-mode'], { relativeTo: this.route} );
    }
}