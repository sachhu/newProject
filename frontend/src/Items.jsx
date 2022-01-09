import { Component } from "react";
import {Item} from "./Item";

export class Items extends Component{
    state = {
        "items": [
            {
                "id": 1,
                "name": "shoes",
                "price": 4444,
                "quantity": 3,
                "sid": 1
            },
            {
                "id": 2,
                "name": "coat",
                "price": 222,
                "quantity": 2,
                "sid": 1
            },
            {
                "id": 4,
                "name": "gorg",
                "price": 333,
                "quantity": 2,
                "sid": 1
            }
        ]
    }
    render(){
        return(
        <div className="container-fluid">
        <div className="row">
            {this.state.items.map((prod) => {
                return <Item key = {prod.id} id={prod.id} name={prod.name} price={prod.price} quantity={prod.quantity} sid={prod.sid} />
            })}
        </div>
        </div>
        )
    }
}