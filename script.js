let totalTime = 120; // 2 minutes in seconds
let timerDisplay = document.getElementById("timer");
let instruction = document.getElementById("instruction");

function updateTimer() {
    let minutes = Math.floor(totalTime / 60);
    let seconds = totalTime % 60;

    seconds = seconds < 10 ? "0" + seconds : seconds;

    timerDisplay.textContent = minutes + ":" + seconds;

    if (totalTime <= 0) {
        clearInterval(timerInterval);
        instruction.textContent = "Session Complete 🌸";
    }

    totalTime--;
}

function updateInstruction() {
    instruction.textContent =
        instruction.textContent === "Inhale Slowly..."
        ? "Exhale Gently..."
        : "Inhale Slowly...";
}

let timerInterval = setInterval(updateTimer, 1000);
setInterval(updateInstruction, 4000);