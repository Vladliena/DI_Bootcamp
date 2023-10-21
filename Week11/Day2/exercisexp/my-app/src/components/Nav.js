import { useState, useContext } from "react"
import { ThemeContext } from './ThemeContext.js'


const Nav = () => {

    const { theme } = useContext(ThemeContext)

    return (
        <header style={theme === 'light' ? { backgroundColor: 'beige' } : { backgroundColor: 'black' }}>
            <nav>
                <ul style={theme === 'light' ? { color: 'grey' } : { color: 'beige' }}>
                    <li>Home</li>
                    <li>About</li>
                    <li>Contacts</li>
                </ul>
            </nav>
        </header>
    )
}

export default Nav