const mongoose = require('mongoose')

const bcrypt = require('bcrypt')

mongoose.connect('mongodb://localhost:27017/blog', {useNewUrlParser: true})

var UserSchema = mongoose.Schema({
    username: {
        type: String,
        required: true
    },
    password: {
        type: String,
        required: true
    },
});

var PostSchema = mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    content: {
        type: String,
        required: true
    },
    author: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'user'
    }

})

UserSchema.statics.authenticate = function (username, password, callback) {
    UserModel.findOne({username: username})
        .exec( (err, user) => {
            if (err) {
                callback(err)
            } else {
                bcrypt.compare(password, user.password, (err, result) => {
                    if (result == true) {
                        return callback(err, user)
                    } else {
                        let err = new Error("Wrong password")
                        err.status = 401
                        callback(err)
                    }
                })
            }
        })
}

const UserModel = mongoose.model('user', UserSchema)

const PostModel = mongoose.model('post', PostSchema)

module.exports = { UserModel, PostModel }