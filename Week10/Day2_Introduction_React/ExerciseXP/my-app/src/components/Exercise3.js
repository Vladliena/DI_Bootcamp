import './Exercise.css'

const Exercise = () => {
    // const style = {
    //     color: "red",
    //     background: "lightblue"
    // }
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };
    return (
        <>
            <h1 style={style_header}>Hello</h1>
            <p className='para'>Tell me more about yourself</p>
            <a href='https://www.cnet.com/a/img/resize/20d6844768bd3f5f0df41deee97897423bcaf3c5/hub/2021/11/03/3c2a7d79-770e-4cfa-9847-66b3901fb5d7/c09.jpg?auto=webp&fit=crop&height=1200&width=1200'>funny image</a>
            <img src='https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg?crop=0.752xw:1.00xh;0.175xw,0&resize=1200:*'></img>
            <form>
                <input type='text' placeholder='tell me your name'></input>
            </form>
            <ul>
                <li>cat</li>
                <li>dog</li>
                <li>bird</li>
            </ul>
        </>
    )
}

export default Exercise