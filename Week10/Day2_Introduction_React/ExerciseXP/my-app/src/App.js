import logo from './logo.svg';
import './App.css';
import user from './data';
import UserFavoriteAnimals from './components/UserFavoriteAnimals';
import Exercise from './components/Exercise3';

function App() {
  const myelement = <h1>I Love JSX!</h1>
  const sum = 5 + 5
  return (
    <div>
      <h3>{user.firstName}</h3>
      <h3>{user.lastName}</h3>
      {myelement}
      <p>"React is {sum} times better with JSX"</p>
      <UserFavoriteAnimals info={user.favAnimals}/>
      <Exercise />
    </div>
  );
}

export default App;
