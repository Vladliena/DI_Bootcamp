import React from "react"

class BuggyCounter extends React.Component {
    constructor() {
        super();
        this.state = {
            counter: 0,
        };
        // this.handleClick = this.handleClick.bind(this)
    }

    handleClick = () => {
        this.setState({ counter: this.state.counter + 1 })
    }
    render() {
        return (
            <>
                <div onClick={this.handleClick}>{this.state.counter > 5 ? (function () { throw new Error("I crashed") }()) : this.state.counter}</div>
                {console.log(this.state.counter)}
            </>
        )
    }
}

export default BuggyCounter