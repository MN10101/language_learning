// Clear cookies function
function clearCookies() {
    document.cookie.split(";").forEach((c) => {
        document.cookie = c
            .replace(/^ +/, "")
            .replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
    });
}

// Handle status updates
document.addEventListener("DOMContentLoaded", function () {
    if (isUserLoggedIn()) {
        const storedStatus = localStorage.getItem("userStatus") || "online";
        setStatus(storedStatus);
    }

    const hamburgerMenu = document.querySelector('.hamburger-menu');
    hamburgerMenu.addEventListener('click', toggleMenu);
    hamburgerMenu.addEventListener('touchstart', toggleMenu);

    // Initialize Flatpickr
    flatpickr("#id_scheduled_start_time", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        altInput: true,
        altFormat: "F j, Y H:i",
        time_24hr: true
    });
    flatpickr("#id_scheduled_end_time", {
        enableTime: true,
        dateFormat: "Y-m-d H:i",
        altInput: true,
        altFormat: "F j, Y H:i",
        time_24hr: true
    });

    // Load status from the server when the page loads
    fetch("/user_status/")
        .then(response => response.json())
        .then(data => {
            if (data.status) {
                localStorage.setItem("userStatus", data.status);
                setStatus(data.status);
            }
        })
        .catch(error => console.error("Error loading user status:", error));
});

// Function to update status
function updateStatus() {
    const selector = document.getElementById("statusSelector");
    const status = selector.value;

    setStatus(status);

    // Save status to localStorage
    localStorage.setItem("userStatus", status);

    // Send status to the backend via AJAX
    fetch("/update_status/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken') // Include CSRF token
        },
        body: JSON.stringify({ 'status': status })
    })
    .then(response => response.json())
    .then(data => {
        if (!data.success) {
            console.error('Failed to update status on the server');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Function to set status visually
function setStatus(status) {
    const profileIcon = document.querySelector(".profile-picture");
    const statusOptions = {
        online: { icon: "🟢", color: "green" },
        busy: { icon: "🔴", color: "red" },
        sleep: { icon: "🟣", color: "purple" },
        offline: { icon: "⚪", color: "gray" },
    };

    if (profileIcon && statusOptions[status]) {
        profileIcon.style.borderColor = statusOptions[status].color;
    }
}

// Helper function to get CSRF token from cookies
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

// Check if the user is logged in
function isUserLoggedIn() {
    return document.cookie.includes("sessionid");
}

// Hamburger menu toggle
function toggleMenu() {
    const navbar = document.querySelector('.navbar');
    navbar.classList.toggle('active');
}

// Dropdown toggle
function toggleDropdown() {
    const dropdownMenu = document.getElementById("dropdownMenu");
    dropdownMenu.classList.toggle("active");
}

// Global click handler to close dropdown if clicking outside
window.onclick = function (event) {
    const dropdownMenu = document.getElementById("dropdownMenu");

    // If the click is outside the dropdown and profile picture, close it
    if (!event.target.closest('.profile-info') && !event.target.closest('.dropdown-menu')) {
        dropdownMenu.classList.remove("active");
    }
};

// Stop propagation of clicks inside the dropdown
document.getElementById("dropdownMenu").addEventListener("click", function (event) {
    event.stopPropagation();
});

// Scroll-to-Top Button Script
const scrollTopBtn = document.getElementById("scrollTopBtn");

window.onscroll = function() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        scrollTopBtn.style.display = "block";
    } else {
        scrollTopBtn.style.display = "none";
    }
};

scrollTopBtn.onclick = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};

// Chatbot functionality
const messageSound = new Audio("/static/sounds/message-alert.mp3");

function toggleChat() {
    const chatbot = document.getElementById("chatbot");
    if (chatbot.style.display === "none" || !chatbot.style.display) {
        chatbot.style.display = "block";
        chatbot.style.animation = "fadeIn 0.3s ease-in-out";
        messageSound.play();  
        addMessage("Chatbot", "Hello! How can I help you today?");  
    } else {
        chatbot.style.animation = "fadeOut 0.3s ease-in-out";
        setTimeout(() => chatbot.style.display = "none", 300);
    }
}

window.onload = function () {
    if (isUserLoggedIn() && !localStorage.getItem('chatbotOpened')) {
        toggleChat();
        localStorage.setItem('chatbotOpened', 'true');
    }
};

function checkEnter(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userInput = inputField.value.trim();

    if (userInput) {
        addMessage("You", userInput);
        inputField.value = '';
        fetchResponse(userInput);
    }
}

function addMessage(sender, message) {
    const chatMessages = document.getElementById("chatbot-messages");
    const messageDiv = document.createElement("div");
    messageDiv.textContent = `${sender}: ${message}`;
    chatMessages.appendChild(messageDiv);
    chatMessages.scrollTop = chatMessages.scrollHeight; 
}

function fetchResponse(question) {
    addMessage("Chatbot", "Thinking...");

    fetch("/chatbot-answer/", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'question': question }),
    })
        .then(response => response.json())
        .then(data => {
            if (data.answer) {
                addMessage("Chatbot", data.answer);
            } else {
                addMessage("Chatbot", "Sorry, I couldn't understand that.");
            }
        })
        .catch(error => {
            console.error('Error:', error);
            addMessage("Chatbot", "Sorry, something went wrong.");
        });
}
