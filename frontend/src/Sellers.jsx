import React, { Component } from "react";
import {Seller} from "./Seller";


export class Sellers extends Component{
    constructor(props){
        super(props);
        this.state = {
            "seller":[]
        }
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
    componentDidMount(){
        var promise = fetch("http://localhost:5000/seller", {method:"GET"});
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