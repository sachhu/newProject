import React, { Component } from "react";
import {Seller} from "./Seller";

export class Sellers extends Component{
    state = {
        "seller": [
            {
                "address": null,
                "email": "sachin@gmail.com",
                "id": 1,
                "name": "Sachin",
                "phone": null,
                "public_id": "c55d0688-6b85-42d1-bf84-3fb1f69c869b"
            },
            {
                "address": "new gali",
                "email": "newemail@gmail.com",
                "id": 5,
                "name": "Kumar",
                "phone": "99999999",
                "public_id": "93afb909-6d06-48de-9b77-dcf2ab5037c1"
            }
        ]
    }
    render(){
        return (
                <div className="container-fluid">
                <h4 className="p-5">
                    Seller List
                </h4>
                <div className="row">
                    {this.state.seller.map((prod) => {
                        return <Seller key={prod.id} id={prod.id} name={prod.name} address={prod.address}/>;
                    })}
                </div>
            </div>
        )
    }
}