const jwt = require('jsonwebtoken')

const { UserModel } = require("../db")

class AuthController {

     static auth(req, res) {
         let username = req.body.username
         let password = req.body.password

         UserModel.authenticate(username, password, (err, user)=> {
             if (err) {
                 err.status = 401 
                 res.sendStatus(401)
             } else {
                 let payload = { id: user._id }
                 const token = jwt.sign(payload, process.env.SECRET_JWT_KEY, {expiresIn: '1800s'})
                 res.json(token)
             }
         })
     }

}

module.exports = { AuthController }