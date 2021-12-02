const { PostModel, UserModel } = require('../db')


class PostController {

    static create(req, res) {
        let data = req.body

        data.author = req.user.id

        PostModel.create(data)
            .then(data => {
                res.send(data)
            })
            .catch(err => {
                res.status(400).send({
                    message: err.message
                })
            })
    }

    static findMyPosts(req, res) {
        var query = PostModel.
            find({"author": req.user.id})

        query.exec(function (err, posts) {
            if (err) { 
                res.sendStatus(404)
            } else {
                res.send(posts)
            }
        })
    }

}

module.exports = { PostController }