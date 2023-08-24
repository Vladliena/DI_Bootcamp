const robots = [
    {
        id: 1,
        name: 'Leanne Graham',
        username: 'Bret',
        email: 'Sincere@april.biz',
        image: 'https://robohash.org/1?200x200'
    },
    {
        id: 2,
        name: 'Ervin Howell',
        username: 'Antonette',
        email: 'Shanna@melissa.tv',
        image: 'https://robohash.org/2?200x200'
    },
    {
        id: 3,
        name: 'Clementine Bauch',
        username: 'Samantha',
        email: 'Nathan@yesenia.net',
        image: 'https://robohash.org/3?200x200'
    },
    {
        id: 4,
        name: 'Patricia Lebsack',
        username: 'Karianne',
        email: 'Julianne.OConner@kory.org',
        image: 'https://robohash.org/4?200x200'
    },
    {
        id: 5,
        name: 'Chelsey Dietrich',
        username: 'Kamren',
        email: 'Lucio_Hettinger@annie.ca',
        image: 'https://robohash.org/5?200x200'
    },
    {
        id: 6,
        name: 'Mrs. Dennis Schulist',
        username: 'Leopoldo_Corkery',
        email: 'Karley_Dach@jasper.info',
        image: 'https://robohash.org/6?200x200'
    },
    {
        id: 7,
        name: 'Kurtis Weissnat',
        username: 'Elwyn.Skiles',
        email: 'Telly.Hoeger@billy.biz',
        image: 'https://robohash.org/7?200x200'
    },
    {
        id: 8,
        name: 'Nicholas Runolfsdottir V',
        username: 'Maxime_Nienow',
        email: 'Sherwood@rosamond.me',
        image: 'https://robohash.org/8?200x200'
    },
    {
        id: 9,
        name: 'Glenna Reichert',
        username: 'Delphine',
        email: 'Chaim_McDermott@dana.io',
        image: 'https://robohash.org/9?200x200'
    },
    {
        id: 10,
        name: 'Clementina DuBuque',
        username: 'Moriah.Stanton',
        email: 'Rey.Padberg@karina.biz',
        image: 'https://robohash.org/10?200x200'
    }
];

function createCards(element) {
    let card = document.createElement('div')
    card.classList = 'col'
    card.innerHTML = `<div class='card h-100 text-center p-1'>
        <img src='${element.image}' class="d-block w-50 m-auto">
        <h5 class="card-title">${element.name}</h5>
        <p class="card-text">${element.email}</p>
        </div>`;
    return card;
}

function renderCard(robots) {
    const cardLayout = document.getElementsByClassName('card_layout')[0]
    robots.forEach((element) => {
        const robotCard = createCards(element)
        cardLayout.append(robotCard)
    })
}

const search = document.getElementsByTagName('input')[0]

function getCards(searchText) {
    const robotCards = document.querySelectorAll('.col');
    robotCards.forEach((card) => {
        const robotName = card.querySelector('.card-title').textContent.toLowerCase();
        const robotEmail = card.querySelector('.card-text').textContent.toLowerCase();
        card.style.display = robotName.includes(searchText) || robotEmail.includes(searchText) ? 'block' : 'none'

    })
}

renderCard(robots)
search.addEventListener('keyup', () => {
    let searchText = search.value.toLowerCase()
    getCards(searchText)
})