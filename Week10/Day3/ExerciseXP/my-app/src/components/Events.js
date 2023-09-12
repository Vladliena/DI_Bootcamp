import { useState } from "react"

const Events = () => {
    const [isToggleOn, setisToggleOn] = useState(true)
    const clickMe = () => {
        alert('I was clicked')
    }

    const handleKeyDown = (event) => {
        if (event.key === 'Enter') {
            alert(`the Enter key was pressed, your input is ${event.target.value}`)
        }
    }
    return (
        <div>
            <button onClick={() => setisToggleOn(!isToggleOn)}>{isToggleOn ? 'ON' : 'OFF'}</button>
            <input placeholder="type something.." onKeyDown={handleKeyDown}></input>
            <button onClick={clickMe}>Click Me!</button>
        </div>
    )
}

export default Events