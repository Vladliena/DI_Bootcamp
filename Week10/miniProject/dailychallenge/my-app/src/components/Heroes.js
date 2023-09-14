import heroes from '../superHeroes.json'
import { useState, useEffect } from "react";
import './Heroes.css'



const Heroes = () => {
    const [superHeroes, setSuperHeroes] = useState()
    const [score, setScore] = useState({
        score: 0,
        totalScore: 0
    })

    useEffect(() => {
        setSuperHeroes(heroes.superheroes)
    }, [])

    function game(id) {
        
    }


    return (
        <>
            <header style={{ backgroundColor: 'red' }}>
                <h1>Superheroes Memory Game</h1>
                <span>Score:{score.score}  |  Total Score:{score.totalScore}</span>
            </header>
            <div style={{ backgroundColor: 'red', marginTop: '10px' }}>Get points by clicking on an image but don't click on any more than once!</div>
            <div className='wrapper'>
                {superHeroes && superHeroes.map((item) => {
                    return (
                        <div onClick={() => game(item.id)} name='card' className="card" style={{ width: '200px', height: '300px', padding: '10px', margin: "15px", border: '1px grey solid', position: 'relative', textAlign: 'left' }}>
                            <div style={{ textAlign: 'center' }}>
                                <img alt='img' src={item.image} style={{ width: '60%' }}></img>
                            </div>
                            <h4>Name: {item.name}</h4>
                            <p>Occupation: {item.occupation}</p>
                        </div>
                    )
                })}
            </div>
        </>
    )

}


export default Heroes