import { Component } from "react";
import { useParams } from "react-router-dom";
import {Item} from "./Item";

export const Itm = () => {
    const params = useParams();
    return <Items sid = {params.sid} />
}

export class Items extends Component{
    constructor(props){
        super(props);

        this.sid = this.props.sid;
        this.state = {
            "items": [
            ]
        }
    }
    render(){
        return(
        <div className="container-fluid">
            {console.log(this.sid)}
        <div className="row">
            {this.state.items.map((prod) => {
                return <Item key = {prod.id} id={prod.id} name={prod.name} price={prod.price} quantity={prod.quantity} sid={prod.sid} />
            })}
        </div>
        </div>
        )
    }

    componentDidMount(){
        var promise = fetch("http://localhost:5000/item/" + this.sid, {method:"GET"});
        promise.then((response) => {
            console.log(response);

            var promis2 = response.json();
            promis2.then((product)=>{
                console.log(product);

                this.setState(product);
              
            })
        });

    }
}