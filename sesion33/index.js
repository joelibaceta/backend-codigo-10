const express = require('express');
const bodyParser = require('body-parser')
const dotenv = require('dotenv')

const { UserController } = require('./controllers/user_controller')
const { AuthController } = require('./controllers/auth_controller')
const { PostController } = require('./controllers/post_controller')

const jwtmiddleware = require('./middlewares/jwt_middleware')

dotenv.config()

const app = express();

app.use(bodyParser.json())

app.get('/', (req, res) => {
    res.send('Hello World')
});

app.post('/signup', UserController.signup)
app.post('/login', AuthController.auth)

app.post('/posts', jwtmiddleware, PostController.create)
app.get('/posts/me', jwtmiddleware, PostController.findMyPosts)

app.listen(3000, () => {
    console.log("Server running...")
})