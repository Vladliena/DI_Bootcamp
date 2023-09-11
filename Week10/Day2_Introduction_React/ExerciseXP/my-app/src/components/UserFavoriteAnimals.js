const UserFavoriteAnimals = (props) => {
    const { info } = props
    console.log(props)
    return (
        <ul>
            {info.map((item,index) => {
                return <li key={index}>{item}</li>
            })}</ul>
    )



}

export default UserFavoriteAnimals