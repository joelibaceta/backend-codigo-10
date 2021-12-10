class BusEventHandlers {

    static handle(e, msg, channel) {
        let event_handlers = {
            "service-loaded": BusEventHandlers.onServiceLoad,
            "user-logged": BusEventHandlers.onBannedUserDetector
        }
        event_handlers[e](msg, channel);
    }

    static onServiceLoad(message, channel) {
        //if (err) console.error(err.message)
        console.log("A new service has been loaded: " + message)
    }

    static onBannedUserDetector(message, channel) {
        console.log(message)
        if (message == "user1") {
            console.log("Alert: " + message + "session has been detected")
            channel.publish("user_banned_detected", message)
        }
    }


}

module.exports = { BusEventHandlers }