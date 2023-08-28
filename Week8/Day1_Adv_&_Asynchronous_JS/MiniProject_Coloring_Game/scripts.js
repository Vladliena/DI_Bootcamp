var grid = document.getElementById("grid");
generateGrid();
let selectedColor = ''

function generateGrid() {
    grid.innerHTML = "";
    for (var i = 0; i < 25; i++) {
        row = grid.insertRow(i);
        for (var j = 0; j < 40; j++) {
            cell = row.insertCell(j);
        }
    }
}

const colorPick = document.getElementById('color_pick')

function createColorOption(color) {
    const colorDiv = document.createElement('div');
    colorDiv.classList.add('color');
    colorDiv.style.backgroundColor = color;
    colorDiv.addEventListener('click', () => {
        selectedColor = color;
        updateColor();
    });
    colorPick.appendChild(colorDiv);
}

function updateColor() {
    const colorDivs = document.querySelectorAll('.color');
    colorDivs.forEach(div => div.classList.remove('selected'));
    const selectedColorDiv = document.querySelector(`.color[style="background-color: ${selectedColor};"]`);
    selectedColorDiv.classList.add('selected');
    console.log(selectedColor)
}

const colors = ['black', 'red', 'blue', 'green', 'yellow', 'purple', 'grey', 'brown', 'pink', 'orange', 'white', 'lightblue', 'darkblue', 'lightgreen'];
colors.forEach(color => createColorOption(color));