import logo from './logo.svg';
import './App.css';
import React, { useEffect } from "react"

import NewItemModal from "./components/modals"

import axios from "axios";

function App() {
  const todoItemsData = [
    {
        "id": 3,
        "title": "Otra Tarea de prueba",
        "user_id": 2,
        "status": 1
    },
  ];
  
  const [todoItems, setTodoItems] = React.useState(todoItemsData);
  const [modal, setModal] = React.useState(false)
  const [newTask , setNewTask] = React.useState("")

  function showModal() {
    setModal(true) 
  }
  function dimissModal() { 
    setModal(false)
  }
  function onChangeInput(value) {
    setNewTask(value)

  }
  function checkHandler(value, id) {
    let final_url = "http://localhost:8000/task/" + id;
    axios.put(final_url, {
      "status": value
    }, {
      headers: {
        'Authorization': 'Token 9e98f52d8815a5f397503b7ea49d53a59e50ecc3'
      }
    })
    .then((res)=> refresh())
    .catch((err) => console.log(err));
  }
  function addTask() {
    axios.post("http://localhost:8000/tasks/", {
      "title": newTask
    },
    {
      headers: {
        'Authorization': 'Token 9e98f52d8815a5f397503b7ea49d53a59e50ecc3'
      }
    })
    .then((res)=> refresh())
    .catch((err) => console.log(err));

  }
  function deleteTask(id) {
    let final_url = "http://localhost:8000/task/" + id;
    axios.delete(final_url,
    {
      headers: {
        'Authorization': 'Token 9e98f52d8815a5f397503b7ea49d53a59e50ecc3'
      }
    })
    .then((res)=> refresh())
    .catch((err) => console.log(err));

  }
  function refresh() { 
    axios.get("http://localhost:8000/tasks/", {
      headers: {
        'Authorization': 'Token 9e98f52d8815a5f397503b7ea49d53a59e50ecc3'
      }
    })
       .then((res) =>setTodoItems(res.data))
       .catch((err) => console.log(err));
  }
  useEffect(()=>{
    refresh()
  }, [])
  return (
    <div className="App">
      <h1>ToDo App</h1>
      <div className="row">
        <div className="col-md-6">
          
          
        </div>
      </div>
      <div className="row">
        <div className="col-md-3">
        </div>
        <div className="col-md-3">
          <input 
            className="form-control" 
            value={newTask} 
            onChange={e => onChangeInput(e.target.value)}
          /> 
        </div>
        <div className="col-md-3">
          <button className="btn btn-primary" onClick={addTask}>
            Agregar Tarea
          </button>
        </div>
      </div>
      <div className="row">

        <table className="table">
          {todoItems.map((item) => {
              return(
                <tr>
                  <td>
                    <input 
                        className="form-control" 
                        type="checkbox" 
                        onChange={ e => { checkHandler(e.target.checked, item["id"]) } }
                        checked={item["status"]}/>
                  </td>
                  <td>
                    {item["id"]}
                  </td>
                  <td>
                    {item["title"]}
                  </td>
                  <td> 
                    <button 
                      className="btn btn-sm btn-danger" 
                      onClick={ e => deleteTask(item["id"])}
                      >
                        Eliminar
                    </button>
                  </td>
                </tr>
              )
            })
          }
        </table>
      </div>
      {modal ? (
        <NewItemModal cancelCallback={dimissModal}/> 
      ) : null}
      
    </div>
  );
}

export default App;
