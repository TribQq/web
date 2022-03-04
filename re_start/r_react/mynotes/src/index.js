import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import App from "./App";
import Expenses from "./routes/expenses";
import Invoices from "./routes/invoices";
import Note from "./routes/note";
import Header from "./components/Header";
import TestList from "./pages/TestList";

// <App/> == этот компонент сам генерирует свои роуты и => может быть базой для этих роутов
const rootElement = document.getElementById("root");
render(
  <BrowserRouter>
    <App/>
  </BrowserRouter>,
  rootElement

);


