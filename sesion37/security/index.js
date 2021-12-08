 
const express = require('express')

const Redis = require('ioredis');

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
    if (channel == "service-loaded") {
        onServiceLoad(message)
    } 
    if (channel == "user-logged") {
        console.log(message)
        if (message == "user1") {
            console.log("Alert: " + message + "session has been detected")
        }
    }
})

app.get('/', (req, res) => {
    res.send('Hello World')
    
})

function onServiceLoad(message) {
    //if (err) console.error(err.message)
    console.log("A new service has been loaded: " + message)
}

app.listen(port, () => {
    console.log('Auth Server Listening')
    pubredis.publish("service-loaded", "security service")
    //redis.publish("service-loaded", "auth service")
})