import database from '../Complexdatabase.json'
import { useState, useEffect } from "react"

const Example2 = () => {

    const [skills, setSkills] = useState()

    useEffect(() => {
        setSkills(database.Skills)
    }, [])

    return (
        <div>
            {skills && skills.map(item => {
                return (
                    <>
                        <div>{item.Area}</div>
                        <ul>
                            {item.SkillSet.map(skill => {
                                return (
                                    <li>{skill.Name}</li>
                                )
                            })}
                        </ul>
                    </>
                )
            })}
        </div>
    )

}

export default Example2