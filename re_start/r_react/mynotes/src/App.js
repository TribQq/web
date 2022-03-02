
import './App.css';
import Header from './components/Header'
import Body from './components/Body';
import { NotesListPage } from './pages/NotesListPage';

function App() {
  return (
    <div className="App">
     <Header />
     <Body />
     <NotesListPage/>
    </div>
  );
}

export default App;
