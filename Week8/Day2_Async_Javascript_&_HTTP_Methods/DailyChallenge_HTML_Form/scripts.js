function pushToDom(event) {
    event.preventDefault()
    document.body.innerHTML += JSON.stringify({ name: event.target.fname.value, secondname: event.target.sname.value })
}