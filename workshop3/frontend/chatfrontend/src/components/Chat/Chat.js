import React, { Component } from 'react'
import WebSocketIntance from '../../services/websockets';
//import './chat.scss'

import WebSocketInstance from '../../services/websockets'

export default class Chat extends Component {

 

    constructor(props) {
        super(props);
        this.state = {
            messages: []
        }
        let self = this;
        WebSocketInstance.connect()
        WebSocketInstance.callbacks["newMessageCallback"] = (payload) => {this.onNewMessageHandler(self, payload)}
    }

    onChangeMessageHandler = (e) => {
        
        this.setState({
            message: e.target.value
        })
    }

    onNewMessageHandler(ref, payload) {
        console.log("Callback")
        console.log(payload)
        if (payload["event"] == "NEW_MESSAGE") {
            let messages = ref.state.messages
            console.log(payload["message"])
            messages.push(payload["message"])
            ref.setState({
                messages: messages
            })
        } 
        if (payload["event"] == "GET_MESSAGES") {
            let messages = payload["message"]
            console.log(messages)
        }
    }
    
    getMessagesHandler() {
        let data = {
            "event": "GET_MESSAGES",
            "message": {}
        }
        WebSocketIntance.sendMessage(data)
    }

    componentDidMount() {
        //this.getMessagesHandler()
    }

    sendMessageHandler(username, message) {
        let data = {
            "event": "NEW_MESSAGE",
            "message": {
                "username": username,
                "content": message
            }
        }
        WebSocketIntance.sendMessage(data)
    }
 

    render() {
        const messages = this.state.messages;
        const currentUser = this.props.currentUser;

        return (
            <div className="chat">
                <div className="container">
                    <h1>Chatting as : {currentUser}</h1>
                    <button onClick={this.getMessagesHandler}>Refresh </button>
                    <ul>
                         {this.state.messages.map((message) => {
                                return <li>{message["username"]} {message["content"]}</li>
                        })}
                    </ul>

                    <div className="container">

                        <input onChange={(e) => this.onChangeMessageHandler(e)} type="text"/>
 
                        <button onClick={() => this.sendMessageHandler(currentUser, this.state.message)} >Send</button>
                    </div>
                </div>
            </div>
        )
    }
}