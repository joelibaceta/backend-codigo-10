

class AuthChannels {
    
    static manage(channel, message) {

        if (channel == "service-loaded") {
            AuthChannels.onServiceLoad(message)
        }
        if (channel == "user_banned_detected") {
            AuthChannels.onUserBannedDetected(message)
        }
    }

    static onServiceLoad(message) {
        //if (err) console.error(err.message)
        console.log("A new service has been loaded: " + message)
    }

    static onUserBannedDetected(message){
        // Cambiar status de usuario
        console.log(message + " user status changed to inactive")
    }

}

module.exports = {AuthChannels}