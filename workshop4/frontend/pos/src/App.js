
import './App.css'; 
import Sidebar from './components/sidebar';
import PosArea from './components/posarea';

function App() {
  return (
    <div className="App hide-print flex flex-row h-screen antialiased text-blue-gray-800">
        <Sidebar></Sidebar>
        <PosArea></PosArea>
    </div>
  );
}

export default App;
