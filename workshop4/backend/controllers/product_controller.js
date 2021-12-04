const {ProductModel} = require('../db')

class ProductController {

    static findAll(req, res) {
        let query = ProductModel.find({})
        query.exec(function (err, products) {
            if (err) {
                res.sendStatus(404)
            } else {
                res.send(products)
            }
        })
    }

    static create(req, res) {
        let data = req.body
        ProductModel.create(data)
            .then(data=> {
                res.send(data)
            })
            .catch(err=>{
                res.status(400).send({
                    message: err.message
                })
            })
    }
}

module.exports = { ProductController }

