import logo from './logo.svg';
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import Home from './components/Home';
import Profile from './components/Profile';
import Shop from './components/Shop';
import PostList from './components/PostList';
import Example1 from './components/Example1';
import Example2 from './components/Example2';
import Example3 from './components/Example3';
import { Routes, Route, NavLink } from "react-router-dom";
import ErrorBoundary from './components/ErrorBoundary';



// const data = {
//   key1: 'myusername',
//   email: 'mymail@gmail.com',
//   name: 'Isaac',
//   lastname: 'Doe',
//   age: 27
// }



function App() {

  const sendData = async () => {
    try {
      const res = await fetch('https://webhook.site/6942b62b-396d-4912-9326-81dca8a717c0', {
        method: 'POST',
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify({
          key1: 'myusername',
          email: 'mymail@gmail.com',
          name: 'Isaac',
          lastname: 'Doe',
          age: 27
        })
      })
      console.log(res)
    } catch (e) {
      console.log(e)

    }
  }
  return (
    <>
      {/* <div className="container">
        <nav className="nav nav-pills">
          <NavLink exact className="nav-link" activeClassName="active" to="/">
            Home
          </NavLink>
          <NavLink className="nav-link" activeClassName="active" to="/profile">
            Profile
          </NavLink>
          <NavLink className="nav-link" activeClassName="active" to="/shop">
            Shop
          </NavLink>
        </nav>
        <Routes>
          <Route path='/' element={
            <ErrorBoundary>
              <Home />
            </ErrorBoundary>
          } />
          <Route path='/profile' element={
            <ErrorBoundary>
              <Profile />
            </ErrorBoundary>
          } />
          <Route path='/shop' element={
            <ErrorBoundary>
              <Shop />
            </ErrorBoundary>
          } />
        </Routes>
      </div> */}


      {/* <PostList /> */}


      {/* <Example1 /> */}

      {/* <Example2 /> */}

      {/* <Example3 /> */}

      <button onClick={sendData}>Send Some Data</button>

    </>
  );
}

export default App;
