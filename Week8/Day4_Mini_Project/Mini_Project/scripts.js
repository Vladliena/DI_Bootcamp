const btn = document.getElementById('btn')
const dataList = document.getElementById('container')
const loader = document.getElementById('loader')
btn.addEventListener('click', findData)



async function findData() {
    dataList.innerHTML = `
    <div class="fa-4x">
    <i id='loader' class="fa-solid fa-spinner fa-spin-pulse fa-spin-reverse"></i>
    </div>
    <span>Loading...</span>`
    let randomNum = Math.round(Math.random() * 83)
    try {
        const response = await fetch(`https://www.swapi.tech/api/people/${randomNum}`)
        if (response.ok) {
            const data = await response.json()
            try {
                const homeworldUrl = data.result.properties.homeworld
                const planetResponse = await fetch(`${homeworldUrl}`)
                if (planetResponse.ok) {
                    const dataPlanet = await planetResponse.json()
                    createList(data, dataPlanet)
                } else {
                    throw new Error('No such planet')
                }
            } catch (err) {
                console.log(err)
            }
        } else {
            throw new Error('No such person')
        }
    } catch (err) {
        console.log(err)
    }
}

function createList(character, planet) {
    dataList.innerHTML = ''
    const { height, gender, birth_year, name } = character.result.properties;
    dataList.innerHTML = `
    <h3> Name: ${name} </h3>
    <p>Height: ${height}</p>
    <p>Gender: ${gender}</p>
    <p>Birth Year: ${birth_year}</p>
    <p>Home World: ${planet.result.properties.name}</p>
    `;
}