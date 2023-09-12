import { useState } from "react"
import Garage from "./Garage"

const Car = (props) => {
    const [color, setColor] = useState('red')
    let size = 'small'
    return (
        <div>
            <Garage info={size} />
            <header>This car is {color} {props.info.model}</header>
        </div>
    )
}

export default Car