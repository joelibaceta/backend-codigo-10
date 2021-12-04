const express = require('express')
const bodyParser = require('body-parser')
const cors = require('cors')

var corsOptions = {
    origin: "*"
}

const { TaskController } = require('./controllers/task_controller')

const app = express()
app.use(bodyParser.json())

app.use(cors())

const port = 5000

app.get('/', (req, res) => {
    res.send('Hello World')
})

app.post('/tasks', TaskController.create)
app.get('/tasks', TaskController.findAll)

app.put('/task/:pk', TaskController.update)
app.delete('/task/:pk', TaskController.delete)

app.listen(port, () => {
    console.log('Server Listening ... ')
})