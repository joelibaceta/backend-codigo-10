const mongoose = require('mongoose')

mongoose.connect('mongodb://localhost:27017/TodoListDB', {useNewUrlParser: true})

var TaskSchema = mongoose.Schema({
    title: {
        type: String,
        required: true
    },
    status: {
        type: String,
        required: false,
        default: "created"
    }
})

const TaskModel = mongoose.model('task', TaskSchema)

module.exports = { TaskModel }

// mongodb://user:password@localhost