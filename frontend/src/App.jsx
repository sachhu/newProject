import React, { Component } from "react";
import { Items } from "./Items";
import {NavBar} from "./NavBar";
import { Sellers } from "./Sellers";
export default class App extends Component{
    state = {

    }
    render(){
        return(
            <React.Fragment>
                <NavBar />
                <Items />

            </React.Fragment>
        )
    }
}