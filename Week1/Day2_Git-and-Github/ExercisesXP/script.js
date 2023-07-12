// let popup = document.querySelectorAll('.popup');
// let popUpText = document.querySelectorAll('.popuptext')


// popup.forEach((element) => {
//     element.addEventListener('click', () => {
//         console.log("mouse over")
//         popUpText.classList.toggle("show")
//         })
//     })

function togglePopup(num) {
    let popup = document.getElementById(`popup-${num}`).classList.toggle("show");
    console.log(`hi ${num}`)

}

