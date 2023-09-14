
import { useState } from 'react'



const Form = () => {

    const [inputs, setInputs] = useState({
        fname: "",
        sname: "",
        age: "",
        gender: "",
        destination: "",
        alergic: []
    })

    const handleChange = (e) => {
        const value = e.target.value
        setInputs({ ...inputs, [e.target.name]: value })
    }


    return (
        <>
            <form>
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
                <input type="checkbox" name="alergic" value="Nuts" onChange={(e) => handleChange(e)} /> Nuts
                <input type="checkbox" name="alergic" value="Lactose" onChange={(e) => handleChange(e)} /> Lactose
                <input type="checkbox" name="alergic" value="VeganMeal" onChange={(e) => handleChange(e)} /> Vegan Meal
                <input type='submit' />
            </form>

            <div>
                <ul>
                    <li>First Name: {inputs.fname}</li>
                    <li>Second Name:{inputs.sname}</li>
                    <li>Age:{inputs.age}</li>
                    <li>Gender:{inputs.gender}</li>
                    <li>Destination{inputs.destination}</li>
                    <li>Alergic: {inputs.alergic}</li>
                </ul>
            </div>
        </>


    )
}


export default Form