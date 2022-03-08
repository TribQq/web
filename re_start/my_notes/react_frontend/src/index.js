import { render } from "react-dom";
import {BrowserRouter, HashRouter} from 'react-router-dom'
// BrowserRouter ==  в джанго юрлс продублировать пути
// HashRouter == дублировать не надо, но передь rout`ами reacta # // example /#/notes/   /#/note/1
// HashRouter путь ссылки #/notes #/note/1  даже  на встроенном порте реакта, 
import React from 'react';
import App from './App';




const rootElement = document.getElementById("root");
render(
  <HashRouter>
    <App/>
  </HashRouter>,
  rootElement

);

