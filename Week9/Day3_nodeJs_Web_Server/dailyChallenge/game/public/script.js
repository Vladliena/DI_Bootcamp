const emojiContainer = document.getElementById('emoji-container');
const emojiElement = document.getElementById('emoji');
const optionsList = document.getElementById('options');
const messageElement = document.getElementById('message');
const scoreElement = document.getElementById('score-value');

function loadNextEmoji() {
    fetch('/game')
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            emojiElement.textContent = data.emoji;

            optionsList.innerHTML = '';
            data.options.forEach((option) => {
                const li = document.createElement('li');
                li.textContent = option;
                li.addEventListener('click', () => guessEmoji(option));
                optionsList.appendChild(li);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}

function guessEmoji(guess) {
    fetch('/guess', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ guess }),
    })
        .then((response) => response.json())
        .then((data) => {
            messageElement.textContent = data.message;
            scoreElement.textContent = data.score;
            loadNextEmoji();
        });
}

loadNextEmoji();