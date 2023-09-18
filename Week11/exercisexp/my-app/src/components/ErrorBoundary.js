import React from "react";

class ErrorBoundary extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            hasError: false,
            error: ''
        }
    }

    componentDidCatch = (error) => {
        console.log(error);
        this.setState({ hasError: true, error: error });
    };

    render() {
        console.log(this.state.error)
        if (this.state.hasError) {
            return (
                <>
                    <h3>{this.state.error.toString()}</h3>
                </>
            )
        } return this.props.children
    }

}

export default ErrorBoundary