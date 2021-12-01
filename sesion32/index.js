const express = require('express');
const bodyParser = require('body-parser')

const { ProductController } = require('./controllers/product_controller')
const { CategoryController } = require('./controllers/category_controller')
const { UserController } = require('./controllers/user_controller')

const { AuthController } = require('./controllers/auth_controller')

const app = express()

app.use(bodyParser.json())

app.post('/products', ProductController.create)
app.get('/products', ProductController.findAll)
app.get('/product/:id', ProductController.findOne)
app.put('/product/:id', ProductController.update)
app.delete('/product/:id', ProductController.destroy)

app.post('/categories', CategoryController.create)
app.get('/categories', CategoryController.findAll)
app.get('/category/:id', CategoryController.findOne)
app.put('/category/:id', CategoryController.update)
app.delete('/category/:id', CategoryController.destroy)

app.post('/signup', UserController.create)
app.post('/signup_sync', UserController.createSync)

app.post('/login', AuthController.login)

app.listen(3000)