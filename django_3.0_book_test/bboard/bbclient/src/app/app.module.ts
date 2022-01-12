import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { BbListComponent } from './bb-list.component';
import { BbDetailComponent } from './bb-detail.component';


import { BbService } from './bb.service'; 
import { FormsModule } from '@angular/forms';
// регаем службу отвечающую за веб-формы 
import { HttpClientModule } from '@angular/common/http';
// imort for 'talk' with backend

import { registerLocaleData } from '@angular/common';
// указывает откуда брать настройки для выбранного языка
import localeRu from '@angular/common/locales/ru';
import loacaleRuExtra from '@angular/common/locales/extra/ru';
import { LOCALE_ID } from '@angular/core';
// берёт дефонлый id языка(по умолчанию eng)
registerLocaleData(localeRu, 'ru', loacaleRuExtra)
// for ru lang 670 page

import { Routes } from '@angular/router';

import { RouterModule } from '@angular/router';

const appRoutes: Routes = [
  {path:':pk', component: BbDetailComponent},
  {path: '', component:BbDetailComponent},  
]
// сохраняем в конст список маршрутов , в типе роутес указав его после двоеточия

@NgModule({
  declarations: [
    AppComponent,
    BbListComponent,
    BbDetailComponent
  ],
  imports: [
    RouterModule.forRoot(appRoutes),
    BrowserModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [BbService, {provide: LOCALE_ID, useValue:'ru'}],
  bootstrap: [AppComponent]
})
export class AppModule { }
