import './App.css';
import Header from './components/Header';
import NotesListPages from './pages/NotesListPages';
import NotePage from './pages/NotePage';

import{Routes,Route} from 'react-router-dom'

function App() {
  return (
    <div className="container dark">
      <div className='app '>
        <Header/>

        <Routes>
          <Route path="nn/:id/:id2" element={<NotesListPages />} />
          <Route path="notes/" element={<NotesListPages />} />
          <Route path="note/:note_id" element={<NotePage />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;
