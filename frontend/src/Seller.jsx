import React, { Component } from "react";

export class Seller extends Component{
    render(){
        return (
            <div className="col-lg-6">
                <div className="card m-2">
                    <div className="card-body">
                        Seller id: {this.props.id}
                        <h4 className="pt-5 border-top">Name: {this.props.name}</h4>
                        <div>Address: {this.props.address}</div>
                    </div>
                
                </div>
            </div>
        )
    }
}