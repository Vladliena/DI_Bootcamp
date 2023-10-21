// Exercise 1

// import React from "react";
// import { ThemeProvider, useTheme } from "./components/ThemeContext";
// import Nav from "./components/Nav";

// function ThemeSwitcher() {
//   const { theme, toggleTheme } = useTheme();

//   return (
//     <div>
//       <button onClick={toggleTheme}>Toggle Theme</button>
//       <p>Current Theme: {theme}</p>
//     </div>
//   );
// }

// function App() {
//   return (
//     <ThemeProvider>
//       <div className="App">
//         <h1>Theme Switcher Example</h1>
//         <ThemeSwitcher />
//         <Nav />
//       </div>
//     </ThemeProvider>
//   );
// }

// export default App;


// Exercise 2

import React, { useRef, useState } from "react";
import "./App.css";

function CharacterCounter() {
  const [txtlength, setTextlength] = useState(0)
  const inputRef = useRef(null);

  const handleInputChange = () => {
    const textLength = inputRef.current.value.length;
    setTextlength(textLength)
    
  };

  return (
    <div>
      <h1>Character Counter</h1>
      <textarea
        ref={inputRef}
        onChange={handleInputChange}
        placeholder="Type something..."></textarea>
      <p>Character Count: {txtlength}</p>
    </div>
  );
}

function App() {
  return (
    <div className="App">
      <CharacterCounter />
    </div>
  );
}

export default App;
