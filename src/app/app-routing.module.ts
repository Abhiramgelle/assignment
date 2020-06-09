import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { DetailslisComponent } from './detailslis/detailslis.component';
import { ProjectComponent } from './project/project.component';
import { ConditionComponent } from './condition/condition.component';
import { Condition1Component } from './condition1/condition1.component';


const routes: Routes = [
  { path: '', component: ProjectComponent },
  { path: 'home', component: ProjectComponent },
  { path: 'detailslis', component: DetailslisComponent },
  { path: 'condition', component: ConditionComponent },
  { path: 'condition1', component: Condition1Component },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
