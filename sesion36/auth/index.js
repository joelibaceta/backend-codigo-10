const express = require('express')

const { UserController } = require('./controllers/user_controller')
const { AuthController } = require('./controllers/auth_controller')

const bodyParse  = require('body-parser')
const app = express()

app.use(bodyParse.json())

app.get('/ping', (req, res) => {
    res.send("pong")
})

app.post('/signup', UserController.create)
app.post('/auth', AuthController.auth)
app.get('/validate', AuthController.validate)


app.listen(3000)