import { useState } from 'react'
import './Form.css'



const Form = () => {

    const [inputs, setInputs] = useState({
        fname: "",
        sname: "",
        age: "",
        gender: "",
        destination: "",
        dietary_nuts: "",
        dietary_lactose: "",
        dietary_veganmeal: ""
    })

    const handleChange = (e) => {
        const value = e.target.type === 'checkbox' ? e.target.checked : e.target.value
        setInputs({ ...inputs, [e.target.name]: value })
    }


    return (
        <>
            <form className='form'>
                <input type='text' name='fname' placeholder='First Name' onChange={(e) => handleChange(e)} />
                <input type='text' name='sname' placeholder='Last Name' onChange={(e) => handleChange(e)} />
                <input type='text' name='age' placeholder='Age' onChange={(e) => handleChange(e)} />
                <div>
                    <input type="radio" name="gender" value="Male" onChange={(e) => handleChange(e)} />Male
                    <input type="radio" name="gender" value="Female" onChange={(e) => handleChange(e)} />Female
                </div>
                <select name="destination" onChange={(e) => handleChange(e)}>
                    <option value="Tel Aviv">Tel Aviv</option>
                    <option value="Odesa">Odesa</option>
                    <option value="New York">New York</option>
                </select>
                <input type="checkbox" name="dietary_nuts" value="Nuts" onChange={(e) => handleChange(e)} /> Nuts
                <input type="checkbox" name="dietary_lactose" value="Lactose" onChange={(e) => handleChange(e)} /> Lactose
                <input type="checkbox" name="dietary_veganmeal" value="VeganMeal" onChange={(e) => handleChange(e)} /> Vegan Meal
                <input type='submit' />
            </form>

            <div className='list'>
                <ul>
                    <li>First Name: {inputs.fname}</li>
                    <li>Second Name:{inputs.sname}</li>
                    <li>Age:{inputs.age}</li>
                    <li>Gender:{inputs.gender}</li>
                    <li>Destination{inputs.destination}</li>
                    <li>Nuts free: {inputs.dietary_nuts? 'ON':'OFF'}</li>
                    <li>Lactose free: {inputs.dietary_lactose? 'ON' : 'OFF'}</li>
                    <li>Vegan Meal: {inputs.dietary_veganmeal? 'ON': 'OFF'}</li>
                </ul>
            </div>
        </>


    )
}


export default Form