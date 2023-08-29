const form = document.getElementById('mainForm')
const btn = document.getElementById('btn')
const containerImage = document.getElementById('container')


form.addEventListener('submit', getData)


async function getData(event) {
    event.preventDefault()
    let userWord = event.target.word.value
    try {
        const response = await fetch(`https://api.giphy.com/v1/gifs/search?q=${userWord}&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My`)
        if (!response.ok) {
            throw new Error('Server doesnt response')
        } else {
            const result = await response.json();
            createImg(result)
        }
    } catch (err) {
        console.log(err)
    }
}

function createImg(data) {
    let gif = data.data[`${Math.round(Math.random() * data.data.length)}`].images.original.url
    const divImg = document.createElement('div')
    const imgEl = document.createElement('img')
    imgEl.style.width = '300px'
    imgEl.setAttribute('src', gif)
    const buttonDel = document.createElement('button')
    buttonDel.innerText = 'Delete'
    divImg.append(imgEl, buttonDel)
    containerImage.append(divImg)
    deleteImg(divImg, buttonDel)
    deleteAll()
}

function deleteImg(img, btn) {
    btn.addEventListener('click', () => {
        img.remove()
    })
}

let buttonCreated = true
function deleteAll() {
    if (buttonCreated) {
        const deleteAllBtn = document.createElement('button')
        deleteAllBtn.innerText = 'Delete All'
        containerImage.appendChild(deleteAllBtn)
        buttonCreated = false
        deleteAllBtn.addEventListener('click', () => {
            buttonCreated = true
            containerImage.innerHTML = ''
        })
    }
}