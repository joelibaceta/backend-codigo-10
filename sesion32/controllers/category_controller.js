const { Category } = require('../models')

class CategoryController {

    static create(req, res) {
        let payload = req.body
        console.log(payload)
        Category.create(payload)
            .then((data) => {
                res.send(data)
            })
            .catch((err) => {
                res.status(400).send({
                    message: err.message
                })
            })
    }

    static findAll(req, res) {
        Category.findAll()
            .then( (data) => {
                res.send(data)
            })
            .catch( (err) => {
                res.status(404).send({
                    "message": err.message
                })
            }) 
    }

    static findOne(req, res) {
        let pk = req.params.id
        Category.findByPk(pk)
            .then( (data) => {
                res.send(data)
            })
            .catch( (err) => {
                res.status(404).send({
                    "message": err.message
                })
            }) 
    }

    static update(req, res) {
        let pk = req.params.id
        let payload = req.body

        Category.update(payload, {where: {id: pk}})
            .then( (data) => {
                res.send(data)
            })
            .catch( (err) => {
                res.status(400).send({
                    "message": err.message
                })
            }) 
    }

    static destroy(req, res) {
        let pk = req.params.id
        Category.destroy({where: {id: pk}})
            .then( (data) => {
                res.status(200).send("DELETED")
            })
            .catch ( (err) => res.status(400).send({
                message: err.message
            }))
    }

}

module.exports = { CategoryController }