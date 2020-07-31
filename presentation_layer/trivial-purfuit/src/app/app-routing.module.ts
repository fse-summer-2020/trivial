import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { GameBoardConfigurationComponent } from './game/gameBoardConfig/gameBoardConfiguration.component';
import { IntroPanelComponent } from './introPanel/introPanel.component';


const routes: Routes = [
  { 
    path: 'game', 
    component: GameBoardConfigurationComponent 
  },
  {
    path: '',
    component: IntroPanelComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
