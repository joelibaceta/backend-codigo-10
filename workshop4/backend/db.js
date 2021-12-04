const mongoose = require('mongoose')
const SchemaTypes = mongoose.Schema.Types

mongoose.connect('mongodb://localhost:27017/posDB', {useNewUrlParser: true})

var ProductSchema = mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    price: {
        type: SchemaTypes.Number,
        default: 0,
        required: true

    },
    picture: {
        type: String,
        required: true
    }
})

var CartItemSchema = mongoose.Schema({
    product: {
        type: SchemaTypes.ObjectId,
        required: true,
        ref: 'product'
    },
    quantity: {
        type: SchemaTypes.Number,
        default: 1
    }
})

const ProductModel = mongoose.model('product', ProductSchema)
const CartItemModel = mongoose.model('cart_item', CartItemSchema)

module.exports = { ProductModel, CartItemModel }