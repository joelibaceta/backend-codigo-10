class WebSocketService {

    static intance = null;

    callbacks = {}


    static getIntance() {
        if (!WebSocketService.intance) {
            WebSocketService.intance = new WebSocketService()
        }
        return WebSocketService.intance
    }

    constructor() {
        this.socketRef = null;
    }

    connect() {
        let path = "ws://localhost:8000/ws/chatroom/"
        this.socketRef = new WebSocket(path)

        this.socketRef.onopen = () => {
            console.log('WebSocket open')
        }
        this.socketRef.onclose = () => {
            console.log('Websocket closed')
            this.connect()
        }

        this.socketRef.onmessage = (e) => {
            const parsedData = JSON.parse(e.data)
            let callback = this.callbacks["newMessageCallback"]
            callback(parsedData["payload"])
        }
        
        
    }

    sendMessage(data) {
        this.socketRef.send(JSON.stringify({...data}))
    }
}

const WebSocketIntance = WebSocketService.getIntance()

export default WebSocketIntance;