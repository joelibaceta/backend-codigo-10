import React, { Component } from 'react'

export default class InitForm extends Component {

    constructor(props) {
        super(props);
        this.state = {
            value: '',
            username: ''
        }
    }

    usernameChangeHandler = (e) => { 
        this.setState({
            username: e.target.value
        })
    }

    render () {
        return (
            <div className="login">
                <p>username: {this.state.username}</p>
                <p>Ingrese su nombre de usuario </p>
                <input type="text" onChange={(e) => this.usernameChangeHandler(e)}></input>
                <button onClick={() => this.props.onSubmit(this.state.username)}>Ingresar</button>

            </div>
        )
    }

}