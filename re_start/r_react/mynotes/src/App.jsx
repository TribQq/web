
import { Routes, Route, Link } from 'react-router-dom';

import NotePage from './pages/NotePage';
import TestList from './pages/TestList';
import { NotesListPage } from './pages/NotesListPage';

function App() {
  return (
  <div>
      <header>
        <Link to="/">Home</Link> | {' '}
        <Link to="/note/:id">Note</Link> | {' '}
        <Link to="/listPage">list_page</Link> | {' '}
      </header>
      <Routes>
        <Route path="/note/:id" element={<NotePage />} />
        <Route path="/listPage" element={<TestList />} />
        <Route path="/NotesListPage/:id" element={<NotesListPage />} />
      </Routes>
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