const {CartItemModel} = require('../db')

class CartController {

    static findAll(req, res) {
        let query = CartItemModel.find({}).populate("product")
        query.exec(function (err, cartitems) {
            if (err) {
                res.sendStatus(404)
            } else {
                res.send(cartitems)
            }
        })
    }

    static create(req, res) {
        let data = req.body
        CartItemModel.create(data)
            .then(data=> {
                res.send(data)
            })
            .catch(err=>{
                res.status(400).send({
                    message: err.message
                })
            })
    }

    static delete(req, res) {
        let pk = req.params.pk
        CartItemModel.findByIdAndDelete(pk)
        .then(data=> {
            res.send("Deleted")
        })
        .catch(err=>{
            res.status(400).send({
                message: err.message
            })
        })
    }
}

module.exports = { CartController }

