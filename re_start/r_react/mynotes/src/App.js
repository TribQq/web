import {
  BrowserRouter as Router,
  Route,
} from "react-router-dom";

import './App.css';
import Header from './components/Header'
import Body from './components/Body';
import {NotesListPage} from './pages/NotesListPage';

function App() {
  return (
    <Router>
    <div className="App">
     <Header />
     <Route path="/" exact component={NotesListPage} />
    </div>
    </Router>
  );
}

export default App;
