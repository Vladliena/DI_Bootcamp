import logo from './logo.svg';
import './App.css';
import Car from './components/Car';
import Events from './components/Events';
import Phone from './components/Phone';
import Color from './components/Color';


function App() {
  const carinfo = { name: "Ford", model: "Mustang" };
  return (
    <div>
      <Car info={carinfo}/>
      <Events />
      <Phone />
      <Color />
    </div>
  );
}

export default App;
