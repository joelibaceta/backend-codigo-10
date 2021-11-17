import { useEffect, useState } from "react"

import axios from "axios";

export default function Main() {

    const [currentUser, setCurrentUser] = useState(null)
    const [loading, setLoading] = useState(true)

    function getCurrentUserData(){
        setLoading(true);
        let getCurrentUserUrl = "http://localhost:8000/api/user/me";
        axios.get(getCurrentUserUrl, {
            headers: {
                'Authorization': 'Bearer ' + localStorage.getItem("token")
            }
        })
        .then((res) => {
            setCurrentUser(res.data)
            console.log(res)
            setLoading(false)
        })
        .catch((err) => {
            console.log(err)
            //setLoading(false)
        })
    }

    useEffect(() => {
        getCurrentUserData()
    }, [])

    function logOut () {
        localStorage.removeItem("token")
    }
    return (
        <div className="form">
            <div className= "row">
                <h1>Home</h1>
            </div>
            { loading ? (
                <span>Loading...</span>
            ) : (
                <div className="row">
                    <p>Welcome {currentUser.first_name} {currentUser.last_name} !</p>
                </div>
            )}
            <button onClick={logOut}>
                Logout
            </button>
        </div>
    )

}