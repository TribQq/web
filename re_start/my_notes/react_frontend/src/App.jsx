import './App.css';
import Header from './components/Header';
import NotesListPage from './pages/NotesListPage';
import NotePage from './pages/NotePage';

import{Routes,Route} from 'react-router-dom'

function App() {
  return (
    <div className="container dark">
      <div className='app '>
        <Header/>
        <Routes>
          <Route path="/notes/" element={<NotesListPage />} />
          <Route path="/note/:note_id" element={<NotePage />} />
        </Routes>

      </div>
    </div>
  );
}

export default App;