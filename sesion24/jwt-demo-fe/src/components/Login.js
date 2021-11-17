import { useState } from "react"

import axios from "axios";

export default function LoginForm() {

    const [email, setEmail] = useState("")
    const [password, setPassword] = useState("")

    const [errors, setErrors] = useState("")
     

    function doLogin(){
        let auth_url = "http://localhost:8000/jwt_login/"
        axios.post(auth_url, {
            "email": email,
            "password": password
        }).then((res) => {
            console.log("OK")
            console.log(res.data.token)
            localStorage.setItem("token", res.data.token)

            //if res.data.role == "admin" {
            //    history.push('/admin')
            //} else {
            //    history.push('/home')
            //}

        }).catch((err) => {
            console.log("ERROR")
            console.log(err.response)
            setErrors(err.response.data.status)
        })
    }

    return (
        <div className="form">
            <div className= "row">
                <h1>Login</h1>
            </div>
            <div>
            { errors != "" ? (
                <div className="alert alert-danger" role="alert">
                    {errors}
                </div>
            ) : null}
            
            </div>
            <div className="row">
                <div className="col-md-4"></div>
                <div className="col-md-4">
                    <div className="form-group">
                        <input placeholder="Username"
                            className="form-control"
                            type="text"
                            value={email}
                            onChange={ e => {
                                setEmail(e.target.value)
                            }}
                        />
                    </div>
                    <div className="form-group">
                        <input placeholder="Password"
                            className="form-control"
                            type="password"
                            value={password}
                            onChange={ e => {
                                    setPassword(e.target.value)
                            }}
                        />
                    </div>
                    <button onClick={doLogin} className="btn btn-light">
                        Login
                    </button>
                </div>
            </div>
        </div>
    )

}