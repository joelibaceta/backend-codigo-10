const bcrypt = require('bcrypt')
const { User } = require('../models')
const jwt = require('jsonwebtoken')

class AuthController {

    static auth(req, res) {
        let authData = req.body 

        User.findOne({where: {email: authData.email}})
            .then((user) => {
                bcrypt.compare(authData.password, user.password)
                    .then((status) => {
                        let payload = {
                            fullname: user.firstName + " " + user.lastName,
                            email: user.email
                        }
                        let token = jwt.sign(payload, "SECRET", {expiresIn: '1800s'})
                        res.json(token)
                    })
                    .catch( err => {
                        res.sendStatus(403)
                    })
            })
            .catch(err => {
                res.sendStatus(401)
            })
    }

    static validate(req, res) {
        const preToken = req.headers['authorization']
        const token = preToken.split(' ')[1]

        jwt.verify(token, "SECRET", (err, payload) => {
            if (err) {
                res.sendStatus(401)
            } else {
                res.status(200).send(payload)
            }
        })
    }

}

module.exports = {AuthController}