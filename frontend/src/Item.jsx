import { Component } from "react";

export class Item extends Component{
    render(){
        return(
            <div className="col-lg-4">
                <div className="card m-2">
                    <div className="card-body">
                        <h4>Name: {this.props.name}</h4>
                        <div>Price: Rs.{this.props.price}</div>
                    </div>
                </div>
            </div>
        );
    }
}