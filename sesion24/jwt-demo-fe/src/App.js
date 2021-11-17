import logo from './logo.svg';
import './App.css';

import LoginForm from './components/Login'
import Main from './components/Main'

function App() {

  function isLogged() {
    if (localStorage.getItem("token") == null) {
      return <LoginForm></LoginForm>
    } else {
      return <Main></Main>
    }
  }
  
  return (
    <div className="App">

       { isLogged() }
    </div>
  );
}

export default App;
