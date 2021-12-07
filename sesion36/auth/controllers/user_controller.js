const bcrypt = require('bcrypt')

const { User } = require('../models')

class UserController {

    static create(req, res) {
        let data = req.body

        bcrypt.genSalt(15, (err, salt) => {
            bcrypt.hash(data.password, salt, (err, hash) => {
                data.password = hash
                User.create(data).then( (data) =>{
                    res.send(data)
                })
                .catch((err) => {
                    res.status(400).send({
                        message: err.message
                    })
                })
            })
        })

    }
}


module.exports = { UserController }