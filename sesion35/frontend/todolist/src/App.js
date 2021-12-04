import logo from './logo.svg';
import './App.css';

import React, { useEffect } from "react"

import axios from "axios"

function App() {

  const [taskList, setTaskList] = React.useState([])
  const [newTaskValue, setNewTaskValue] = React.useState("")
  const [updating, setUpdating] = React.useState("")
  const [editingValue, setEditingValue] = React.useState("")

  function refresh() {
    axios.get("http://localhost:5000/tasks")
      .then((res) => {
        console.log(res.data)
        setTaskList(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
  }

  useEffect(() => {
    refresh()
  }, [])

  function addTask() {
    //taskList.push(newTaskValue)
    axios.post("http://localhost:5000/tasks", {
      "title": newTaskValue
    })
    .then((res) => refresh())
    .catch((err) => console.log(err))

    setNewTaskValue("")
  }

  function onNewTaskValueChange(value) {
    setNewTaskValue(value)
  }

  function remove(id) {
    let url = "http://localhost:5000/task/" + id
    axios.delete(url)
      .then((res) => refresh())
      .catch((err) => console.log(err))
  }

  function checkHandler(value, id) {
    let url = "http://localhost:5000/task/" + id
    axios.put(url, {
      status: boolToStatus(value)
    })
    .then((res) => refresh())
    .catch((err) => console.log(err))

  }

  function boolToStatus(bool) {
    if (bool) {
      return "closed" 
    } else {
      return "created"
    }
  }

  function statusToBool(value) {
    if (value === "created") {
      return false;
    } else {
      return true
    }
  }

  function editedHandler(value, id) {
    let url = "http://localhost:5000/task/" + id
    setUpdating("")
    axios.put(url, {
      title: value
    })
    .then((res) => refresh())
    .catch((err) => console.log(err))
  }

  function isUpdating(id) {
    return updating === id
  }

  function editionHadler(title, id) {
    setEditingValue(title)
    setUpdating(id)
    
  }

  function editionValueHandler(value) {
    setEditingValue(value)
  }

  return (
    <div className="App">
      <h1>Todo List</h1>

      <div>
        <input 
          className="newTaskInput" 
          value={newTaskValue}
          onChange={ e => onNewTaskValueChange(e.target.value)}/>
        <button 
          className="addTaskButton" 
          onClick={addTask}> Agregar Tarea</button>
      </div>
      <br/>
      <center>
        <table  >
          { taskList.map((item) => {
            return(
              <tr>
                <td><input type="checkbox" onChange={e => checkHandler(e.target.checked, item._id)} checked={statusToBool(item.status)}/></td>
                <td>
                  { isUpdating(item._id) ? 
                    (<input 
                      value={editingValue} 
                      onBlur={e => editedHandler(e.target.value, item._id)}
                      onChange={e => editionValueHandler(e.target.value)}/>)
                    : 
                    (<span onDoubleClick={e => editionHadler(item.title, item._id)}>{item.title}</span>) }
                </td>
                <td><button onClick={e => remove(item._id)}>X</button></td>
              </tr>
            )
          }) }
        </table>
      </center>

    </div>
  );
}

export default App;
