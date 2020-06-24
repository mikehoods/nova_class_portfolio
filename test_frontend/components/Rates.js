import React, { Component } from 'react';
class Rates extends Component {
    constructor(props){
        super(props)
        this.state = {
            currency: parseFloat(1).toFixed(2)
        }
    }
    updateCurrency = (event) => {
        this.setState({
            currency: parseFloat(event.target.value).toFixed(2)
        })
    }
    render(){
        return(
            <div>
                <h4>
                    $1 {this.props.rates.base} is worth {this.state.currency} in
                    <select onChange={this.updateCurrency}>
                        {Object.keys(this.props.rates.rates).map((key, index) => {
                            return(
                                <option key={key} value={this.props.rates.rates[key]}>{key}</option>
                            )
                        })}
                    </select>
                </h4>
            </div>
        )
    }
}
export default Rates;