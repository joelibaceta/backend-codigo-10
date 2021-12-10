 
const express = require('express')

const Redis = require('ioredis');
const { BusEventHandlers } = require('./handlers')

const subredis = new Redis()
const pubredis = new Redis()

const app = express()
const port = 3002

subredis.subscribe("service-loaded", () => {
    console.log("Suscribed to service-loaded topic ")
})

subredis.subscribe("user-logged", () => {
    console.log("Suscribed to user-logged topic ")
})

subredis.on("message", (channel, message) => {
    BusEventHandlers.handle(channel, message, pubredis)
})

app.get('/', (req, res) => { res.send('Hello World') })

app.listen(port, () => {
    console.log('Auth Server Listening')
    pubredis.publish("service-loaded", "security service")
    //redis.publish("service-loaded", "auth service")
})