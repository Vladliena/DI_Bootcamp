import logo from './logo.svg';
import './App.css';
import { useState } from "react"

function App() {
  const [languages, setLanguages] = useState([
    { name: "Php", votes: 0 },
    { name: "Python", votes: 0 },
    { name: "JavaSript", votes: 0 },
    { name: "Java", votes: 0 }
  ])

  const increace = (index) => {
    let plusVotes = [...languages]
    plusVotes[index].votes += 1
    setLanguages(plusVotes)
  }
  return (
    <div>
      {languages.map((item, i) => {
        return <div style={{ backgroundColor: "beige", border: "grey 2px solid", padding: "10px", marginBottom: "px", display: "flex", alignItems: "center", justifyContent: "space-between", width: "200px" }}>
          <h2 key={i}>{item.name}</h2>
          <span>{item.votes}</span>
          <button onClick={() => increace(i)}>Click me</button>
        </div>
      })}
    </div>
  );
}

export default App;
