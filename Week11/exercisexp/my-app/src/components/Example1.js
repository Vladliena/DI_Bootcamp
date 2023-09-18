import database from '../Complexdatabase.json'
import {useState,useEffect} from "react"

const Example1 = () => {

    const [social, setSocial] = useState()

    useEffect(() => {
        setSocial(database.SocialMedias)
    }, [])

    return (
        <ul>
        {social && social.map((item) => {
            return(
                <li>{item}</li>
            )
        })}
        </ul>
    )

}

export default Example1