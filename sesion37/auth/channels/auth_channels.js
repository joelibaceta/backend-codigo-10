

class AuthChannels {
    
    static manage(channel, message) {

        if (channel == "service-loaded") {
            AuthChannels.onServiceLoad(message)
        }
    }

    static onServiceLoad(message) {
        //if (err) console.error(err.message)
        console.log("A new service has been loaded: " + message)
    }
}

module.exports = {AuthChannels}