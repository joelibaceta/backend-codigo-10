const { User } = require('../models')

const bcrypt = require('bcrypt')

class UserController {

    static createSync(req, res) { // Bloqueante
        let payload = req.body

        const salt = bcrypt.genSaltSync(10)
        let newPassword = bcrypt.hashSync(payload.password, salt)

        payload.password = newPassword

        User.create(payload)
            .then( (data) => {
                res.send(data)
            })
            .catch( (err) => {
                res.status(400).send({
                    message: err.message
                })
            })

    }
    static create(req, res) {
        let payload = req.body

        bcrypt.genSalt(15, (err, salt) => {
            bcrypt.hash(payload.password, salt, (err, hash) => {
                payload.password = hash;
                User.create(payload).then( (data) => {
                    res.send(data)
                })
                .catch( (err) => {
                    res.status(400).send({
                        message: err.message
                    })
                })
            })
        })
    }

}

module.exports = { UserController }