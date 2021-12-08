const fs = require('fs')



class AuthController {

    static login(req, res, channel) {

        let username = req.body.username
        let password = req.body.password

        fs.readFile('./user.json', (err, data) => {
            if (err) throw err;
            let userData = JSON.parse(data)
            
            userData.forEach(element => {
                
                if (element.username == username) {
                    console.log(element.username)
                    if (element.password == password) {
                        channel.publish("user-logged", username)
                        console.log("logged")
                        return res.send("logged as " + username) 
                        
                    } else {
                        console.log("bad pass")
                        return res.send("login failed")
                    }
                } else {
                    console.log("bad user")
                    //return res.send("login failed")
                }

            });

            
        })
        
    }

     
}

module.exports = {AuthController}