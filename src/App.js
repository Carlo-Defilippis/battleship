import React from 'react';
import logo from './logo.svg';
import './App.css';
import Grid from './components/grid/index'

function App() {
  return (
    <div className="App">
    {/* Jumbotron */}
      <div className="jumbotron">
        <h1 className="display-4">BattleShip!</h1>
        <p className="lead">This is a sample jumbotron for the Battleship Game.</p>
        <hr className="my-4" />
        <p>We can put basic information here.</p>
        <a className="btn btn-primary btn-lg" href="#" role="button">Start a new game!</a>
      </div>
    {/* Grid system */}
    <Grid></Grid>

    {/* Footer */}
      <footer className="footer mt-auto py-3 bg-secondary">
        <div className="container">
          <span className="text-white ">Place sticky footer content here.</span>
        </div>
      </footer>
    </div>
  );
}

export default App;
