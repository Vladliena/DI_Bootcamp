import logo from './logo.svg';
import './App.css';
import React from "react"

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      data: '',
      message: '',
      responseMessage: ''
    }
  }


  async componentDidMount() {
    try {
      const res = await fetch('http://localhost:3000/api/hello')
      const mainMessage = await res.json()
      this.setState({ data: mainMessage })

    } catch (e) {
      console.log(e)
    }
  }


  handleInputChange = (e) => {
    this.setState({ message: e.target.value });
  }

  handleSubmit = async (e) => {
    e.preventDefault()
    try {
      const res = await fetch('http://localhost:3000/api/world', {
        method: 'POST',
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify({ input: this.state.message })
      });
      const data = await res.json();
      console.log(data)
      this.setState({
        responseMessage: data.mesageServer
      })
    } catch (e) {
      console.log(e)
    }


  }
  render() {
    return (
      <>
        <header>
          {this.state.data}
        </header>
        <form onSubmit={this.handleSubmit}>
          <input value={this.state.message} type='text' onChange={this.handleInputChange} />
          <input type='submit' value='Send' />
        </form>
        {this.state.responseMessage && (
          <h3>{this.state.responseMessage}</h3>
        )}
      </>
    );
  }
}

export default App;
