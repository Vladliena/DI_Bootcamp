import logo from './logo.svg';
import './App.css';
import BuggyCounter from './components/BuggyCounter';
import ErrorBoundary from './components/ErrorBoundary';
import Color from './components/Color';

function App() {
  return (
    <div className="App">
      {/* <>
        <ErrorBoundary>
          <BuggyCounter />
          <BuggyCounter />
        </ErrorBoundary>
      </>
      <hr />
      <>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <ErrorBoundary>
          <BuggyCounter />
        </ErrorBoundary>
        <hr />
      </>
      <>
        <BuggyCounter />
      </>
      <hr /> */}

      <Color />
    </div>
  );
}

export default App;
