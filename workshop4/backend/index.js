const express = require('express')
const cors = require('cors')
const bodyParser = require('body-parser')

const {ProductController } = require('./controllers/product_controller')
const {CartController} = require('./controllers/cart_controller')
 
const app = express()
const port = 5000
app.use(bodyParser.json())
app.use(cors())

app.get('/', (req, res) => {
    res.send('Hello World')
})

app.get('/products', ProductController.findAll)
app.post('/products', ProductController.create)

app.get('/cart_items', CartController.findAll)
app.post('/cart_items', CartController.create)
app.delete('/cart_item/:pk', CartController.delete)

app.use('/assets', express.static('assets'))

app.listen(port, ()=> { 
    console.log('Server Running...')
})