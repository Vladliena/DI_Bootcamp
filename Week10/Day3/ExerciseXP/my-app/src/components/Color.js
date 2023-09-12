import { useState, useEffect } from "react"

const Color = () => {
    const [favoriteColor, setfavoriteColor] = useState('red')

    useEffect(() => {
        alert('useEffect reached')
    }, [])
    return (
        <div>
            <header>My favorite color is {favoriteColor}</header>
            <button onClick={() => setfavoriteColor('blue')}>Change to blue color</button>
        </div>
    )
}

export default Color