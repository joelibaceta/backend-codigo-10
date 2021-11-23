import logo from './logo.svg';
import './App.css';
import { Component } from 'react';

import InitForm from './components/InitForm';
import Chat from './components/Chat';

export default class App extends Component {

  constructor(props){
    super(props);
    this.state = {
      username: '',
      loggedIn: false
    }
  }

  handleLoginSubmit = (username) => {
    console.log("onsubmit")
    this.setState({
      loggedIn: true, username: username
    })
  }

  render () {
    return (
      <div>
        {this.state.username}
        { this.state.loggedIn? 
          <Chat currentUser={this.state.username}></Chat>
          : 
          <div className="App">
            <InitForm onSubmit={this.handleLoginSubmit}></InitForm>
          </div>

        }
      </div>
    );
  }
}
 
