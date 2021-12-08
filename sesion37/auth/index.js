 
const express = require('express')
const bodyParser = require("body-parser")

const Redis = require('ioredis');

const {AuthController} = require('./controllers/auth_controller')
const {AuthChannels} = require('./channels/auth_channels')

const subredis = new Redis()
const pubredis = new Redis()

const app = express()
const port = 3001

app.use(bodyParser.json())

subredis.subscribe("service-loaded", () => {
    console.log("Suscribed to service-loaded topic ")
})

subredis.on("message", AuthChannels.manage)

app.get('/', (req, res) => {res.send('Hello World')})

app.post('/login', (req, res) => {
    AuthController.login(req, res, pubredis)
})

app.listen(port, () => {
    console.log('Auth Server Listening')
    pubredis.publish("service-loaded", "auth service")
 
})