 
const { TaskModel } = require('../db')

class TaskController {

    static create(req, res) {

        let data = req.body

        TaskModel.create(data)
            .then(data => {
                res.send(data)
            })
            .catch(err => {
                res.status(400).send({
                    message: err.message
                })
            })

    }

    static findAll(req, res) {
        var query = TaskModel.find({})

        query.exec(function (err, tasks) {
            if (err) {
                res.sendStatus(404)
            } else {
                res.send(tasks)
            }
        })
    }

    static update(req, res) {
        let pk = req.params.pk
        let payload = req.body
        let query = TaskModel.findByIdAndUpdate(pk, payload)

        query.exec(function(err, task) {
            if (err) {
                res.sendStatus(404)
            } else {
                res.send(task)
            }
        })

    }

    static delete(req, res) {
        let pk = req.params.pk
        let query = TaskModel.findByIdAndDelete(pk)
        query.exec(function(err, task) {
            if (err) {
                res.sendStatus(404)
            } else {
                res.send(task)
            }
        })
    }

}

module.exports = { TaskController }