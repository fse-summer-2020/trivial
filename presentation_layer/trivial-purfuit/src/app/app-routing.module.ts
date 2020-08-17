import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { IntroPanelComponent } from './introPanel/introPanel.component';
import { GameBoardConfigurationComponent } from './game/gameBoardConfig/gameBoardConfiguration.component';
import { GameBoardManagerComponent } from './game/gameBoardManager/gameBoardManager.component';
import { ConfigurationPageComponent } from './configuration-page/configuration-page.component';
import { DeterminePlayerOrderComponent } from './determine-player-order/determine-player-order.component';
import { EndGamePageComponent } from './end-game-page/end-game-page.component';


const routes: Routes = [
  { 
    path: 'game-config', 
    component: GameBoardConfigurationComponent 
  },
  {
    path: 'game',
    component: GameBoardManagerComponent
  },
  {
    path: '',
    component: IntroPanelComponent
  },
  {
    path: 'config-mode',
    component: ConfigurationPageComponent
  },
  {
    path: 'player-order',
    component: DeterminePlayerOrderComponent
  },
  {
    path: 'end-game',
    component: EndGamePageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
