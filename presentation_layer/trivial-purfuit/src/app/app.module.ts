import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HttpClientModule } from '@angular/common/http';
import { GameBoardService } from './game/service/gameBoard.service';
import { GameBoardComponent } from './game/gameBoard/gameBoard.component';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { GameBoardConfigurationComponent } from './game/gameBoardConfig/gameBoardConfiguration.component';

@NgModule({
  declarations: [
    AppComponent,
    GameBoardComponent,
    GameBoardConfigurationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
    ],
  providers: [GameBoardService],
  bootstrap: [AppComponent]
})
export class AppModule { }
