const express = require('express')

const app = express()
const port = 3000

app.get('/', (req, res)=>{
    res.send('Hello World');
})

// http://localhost:3000/hello_name?name=Juan
app.get('/hello_name', (req, res)=>{
    let name = req.query.name;
    if (name == undefined) {
        name = "Anonymous"
    }
    res.send(`Hello ${name}`);
})

// http://localhost:3000/hello/:name
app.get('/hello/:name', (req, res) => {
    console.log(req.params)
    let name = req.params.name;
    res.send(`Hello ${name}`);
})

app.listen(port, () => {
    console.log(`Server started on ${port}`)
})
