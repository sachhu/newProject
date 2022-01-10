import React, { Component } from "react";
import { Itm } from "./Items";
import {NavBar} from "./NavBar";
import { Sellers } from "./Sellers";
import {Nofound} from "./Nofound";

import { BrowserRouter, Routes, Route}  from "react-router-dom";

export default class App extends Component{
    state = {

    }
    
    render(){
        return(
            <BrowserRouter>
                <NavBar />
                <Routes>               
                <Route path="/sellers" element={<Sellers />}/>
                <Route path="/seller/:sid" element={<Itm/>}/>
                <Route path="*" element={<Nofound/>} />
                </Routes>
            </BrowserRouter>
        );
    }
}