// const planets = ['Earth','Venus','Uranus','Jupiter','Neptune','Mercury','Saturn','Mars']

const planetsData = [
    { name: 'Earth', moons: 1 },
    { name: 'Venus', moons: 0 },
    { name: 'Uranus', moons: 27 },
    { name: 'Jupiter', moons: 79 },
    { name: 'Neptune', moons: 14 },
    { name: 'Mercury', moons: 0 },
    { name: 'Saturn', moons: 82 },
    { name: 'Mars', moons: 2 }
];

const mainSection = document.querySelector('.listPlanets')

planetsData.forEach((planet) => {
    let planetDiv = document.createElement('div')
    planetDiv.classList = `planet ${planet.name}`
    planetDiv.innerText = planet.name
    for (let i = 0; i < planet.moons; i++){
        let moonDiv = document.createElement('div')
        moonDiv.classList = 'moon'
        moonDiv.innerText = planet.moons
        planetDiv.appendChild(moonDiv)
    }

    mainSection.append(planetDiv)
})