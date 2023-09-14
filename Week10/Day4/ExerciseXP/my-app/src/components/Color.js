import React from "react"



class Child extends React.Component {

    componentWillUnmount() {
        alert('The header was unmounted')
    }

    render() {
        return (
            <header>Hello World</header>
        )
    }
}


class Color extends React.Component {
    constructor() {
        super()
        this.state = {
            favoriteColor: "red",
            show: true
        }
    }

    shouldComponentUpdate() {
        return true
    }


    getSnapshotBeforeUpdate() {
        console.log("in getSnapshotBeforeUpdate")
    }


    componentDidUpdate() {
        console.log('component did update')
    }

    handleClick = () => {
        this.setState({ favoriteColor: 'blue' })
    }
    
    render() {
        if (this.state.show) {
            return (
                <>
                    <Child />
                    <button onClick={() => this.setState({show: false})}>Delete Header</button>
                </>
            )
        }
        // return (
        //     <div>
        //         <header>My favorite color is {this.state.favoriteColor}</header>
        //         <button onClick={this.handleClick}>Change to blue color</button>
        //     </div>
        // )
    }


}

export default Color