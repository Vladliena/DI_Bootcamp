import database from '../Complexdatabase.json'
import { useState, useEffect } from "react"

const Example3 = () => {

    const [experience, setExperience] = useState()

    useEffect(() => {
        setExperience(database.Experiences)
    }, [])

    return (
        <div>
            {experience && experience.map((item, index) => {
                return (
                    <div key={index} style={{display: "flex" , flexDirection: "column"}}>
                        <a href={item.url}>{item.companyName}</a>
                        <img alt='img' src={item.logo} style={{width:"300px"}} />
                        <ul>
                            {item.roles.map((role) => {
                                return (
                                    <>
                                    <li>{role.title}</li>
                                    <li>{role.description}</li>
                                    <li>{role.startDate}</li>
                                    <li>{role.endDate}</li>
                                    <li>{role.location}</li>
                                    </>
                                )
                            })}
                        </ul>

                    </div>
                )
            })}
        </div>
    )

}

export default Example3