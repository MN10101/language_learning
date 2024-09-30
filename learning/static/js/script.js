const words = [
    { word: "Apple", definition: "A fruit that is red or green.", image: "/static/images/apple.png" },
    { word: "Banana", definition: "A long, yellow fruit.", image: "/static/images/banana.png" },
    { word: "Cherry", definition: "A small, round red fruit.", image: "/static/images/cherry.jpg" },
    { word: "Grapes", definition: "Small round fruits that grow in bunches.", image: "/static/images/grapes.png" },
    { word: "Orange", definition: "A round, orange fruit.", image: "/static/images/orange.jpg" },
    { word: "Peach", definition: "A soft fruit with fuzzy skin.", image: "/static/images/peach.jpg" },
];

let currentCardIndex = 0; // Track the current card index

// Create flashcard
function createCard() {
    const flashcardsContainer = document.getElementById("flashcards-container");
    flashcardsContainer.innerHTML = ''; // Clear previous content

    const currentWord = words[currentCardIndex];

    const cardElement = document.createElement("div");
    cardElement.classList.add("card");

    // Show only the definition and the Answer button initially
    cardElement.innerHTML = `
        <div class="card-inner">
            <div class="card-front">
                <p>${currentWord.definition}</p>
                <button class="button show-answer" onclick="showAnswer()">Answer</button>
            </div>
            <div class="card-back hidden">
                <img src="${currentWord.image}" alt="${currentWord.word}">
            </div>
        </div>
    `;

    flashcardsContainer.appendChild(cardElement);
}

// Show answer when button is clicked
function showAnswer() {
    const cardBack = document.querySelector('.card-back');
    const cardFront = document.querySelector('.card-front');
    const clickSound = document.getElementById('click-sound');

    cardBack.classList.remove('hidden'); // Reveal the card back
    cardFront.classList.add('hidden'); // Hide the front side
    clickSound.play(); // Play click sound
}

// Move to the next card
function nextCard() {
    currentCardIndex++;
    const clickSound = document.getElementById('click-sound');

    if (currentCardIndex >= words.length) {
        currentCardIndex = 0; // Reset to the first card after finishing
    }
    createCard(); // Create the new card
    clickSound.play(); // Play click sound
}

// Initialize game
createCard();