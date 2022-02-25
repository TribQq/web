import  React, { Component } from  'react';
import { BrowserRouter } from  'react-router-dom' // BrowserRouter обеспечивает синхронизацию пользовательского интерфейса с URL, используя API истории HTML5.
import { Route, Link } from  'react-router-dom'
import  CustomersList  from  './CustomersList'
import  CustomerCreateUpdate  from  './CustomerCreateUpdate'
import  './App.css';



// Мы используем компонент Route для определения маршрутов нашего приложения; компонент, 
// который должен загружать маршрутизатор после обнаружения совпадения. 
// Для каждого маршрута требуются параметры path для указания пути сопоставления и component 
// для указания загружаемого компонента.
//  Свойство exact указывает маршрутизатору на необходимость точного соответствия пути.
// ()

const BaseLayout = () =>(
  <div className='container-fluid'>
      <nav className='navbar navbar-expand-lg navbar-light bg-light'>
        <a className='navbar-brand' href='#'>Django React Demo</a>
        <button  className="navbar-toggler"  type="button"  data-toggle="collapse" 
        data-target="#navbarNavAltMarkup"  aria-controls="navbarNavAltMarkup"  
        aria-expanded="false"  aria-label="Toggle navigation">
          <span className='navbar-toggler-icon'></span>
        </button>
        <div className='collapse navbar-collapse' id='navbarNavAltMarkup'>
          <div className='navbar-nav'>
            <a className='navbar-nav'>
              <a className='nav-item nav-link' href='/'>CUSTOMERS</a>
              <a className='nav-item nav-link' href='/'>CREATE CUSTOMER</a>
            </a>
          </div>
        </div>
        </nav>
        <div className='content'>
          <Route path='/' exact component={CustomersList} />
          <Route path='/customer/:pk' exact component={CustomerCreateUpdate} />
          <Route path='/customer/' exact component={CustomerCreateUpdate} />
          </div>
    </div>
)

//App - corener component - max lvl in app

class App extends Component{
  render(){
    return(
      <BrowserRouter>
      <BaseLayout/>
      </BrowserRouter>
    );
  }
}
//Мы поместили компонент BaseLayout в компонент BrowserRouter, потому что наше приложение предусматривает работу через браузер.

export default App;



//--------------------------------------------------------------------------------
//deafult setup

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
