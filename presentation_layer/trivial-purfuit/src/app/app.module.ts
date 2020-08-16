import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { GameBoardService } from './game/service/gameBoard.service';
import { AdminService } from './admin.service';
import { GameBoardManagerComponent } from './game/gameBoardManager/gameBoardManager.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { GameBoardConfigurationComponent } from './game/gameBoardConfig/gameBoardConfiguration.component';
import { ConfigurationPageComponent } from './configuration-page/configuration-page.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatDialogModule } from '@angular/material/dialog';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatExpansionModule} from '@angular/material/expansion';
import { EditQuestionDialogComponent } from './edit-question-dialog/edit-question-dialog.component';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatSnackBarModule } from '@angular/material/snack-bar';
import { DeterminePlayerOrderComponent } from './determine-player-order/determine-player-order.component';
import { TokenComponent } from './token/token.component';
import { IntroPanelComponent } from './introPanel/introPanel.component';
import { GameBoardComponent } from './game-board/game-board.component';
import { PlayerCardComponent } from './game/components/playerCard/playerCard.component';
import { EndGamePageComponent } from './end-game-page/end-game-page.component';

@NgModule({
  declarations: [
    AppComponent,
    GameBoardManagerComponent,
    GameBoardConfigurationComponent,
    ConfigurationPageComponent,
    EditQuestionDialogComponent,
    DeterminePlayerOrderComponent,
    TokenComponent,
    IntroPanelComponent,
    GameBoardComponent,
    PlayerCardComponent,
    EndGamePageComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule,
    MatDialogModule,
    MatButtonModule,
    MatInputModule,
    MatExpansionModule,
    MatSelectModule,
    MatFormFieldModule,
    MatSnackBarModule
    ],
  providers: [GameBoardService, AdminService],
  bootstrap: [AppComponent]
})
export class AppModule { }
