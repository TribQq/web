import './App.css';


import { Routes, Route, Link } from 'react-router-dom';

import NotePage from './pages/NotePage';
import TestList from './pages/TestList';
// import { NotesListPage } from './pages/NotesListPage';
import { SinglePage } from './pages/SinglePage';
import NotesListPage from './pages/NotesListPage';
import Header from './components/Header';
function App() {
  return (
  <div className='container dark'>

    <div className='app'>
      <div><Header/></div>
      <div>
      <Link to="/">Home</Link> | {' '}
      <Link to="/note/1">Note</Link> | {' '}
      <Link to="/NotesListPage/1">NotesListPage</Link> | {' '}
      <Link to="/SinglePage/1/2">SinglePage</Link> | {' '}
      </div>

      <Routes>
        <Route path="/" element={<NotesListPage />} />
        <Route path="/note/:noteId" element={<NotePage />} />
        <Route path="/NotesListPage/:id" element={<NotesListPage />} />
        <Route path="/SinglePage/:id/:category_id" element={<SinglePage />} />
      </Routes>
    </div>
  </div>
  );
}


export default App;








// import React from 'react';

// import {
//   BrowserRouter as Router,
//   Link,
//   Route,
//   Routes,
// } from 'react-router-dom';

// import './App.css';
// import Body from './components/Body';
// import Header from './components/Header'
// // import Body from './components/Body';
// import {NotesListPage} from './pages/NotesListPage';
// import NotePage from './pages/NotePage';
// import Note from './routes/note';


// function App() {
//   return (
//     <>
//       <header>
//         <Link to="/">Home</Link>
//         <Link to="/posts">Blog</Link>
//         <Link to="/about">About</Link>
//       </header>
//       <Routes>
//         <Route path="/" element={<Header />} />
//         <Route path="/about" element={<Note />} />
//         <Route path="/posts" element={<Note />} />
//         <Route path="*" element={<Note />} />
//       </Routes>
//     </>
//   );
// }
// export default App;