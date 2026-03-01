const roomRoot = document.getElementById("roomRoot");
const roomCode = roomRoot.dataset.roomCode;
const username = localStorage.getItem("username") || "Guest";
let userId = Number.parseInt(localStorage.getItem("user_id"), 10);
const protocol = window.location.protocol === "https:" ? "wss" : "ws";

const questionBox = document.getElementById("questionBox");
const optionsBox = document.getElementById("optionsBox");
const timer = document.getElementById("timer");
const statusText = document.getElementById("statusText");
const connectionChip = document.getElementById("connectionChip");
const leaderboardBody = document.getElementById("leaderboardBody");
const leaderboardEmpty = document.getElementById("leaderboardEmpty");
const startQuizBtn = document.getElementById("startQuizBtn");

document.getElementById("playerName").textContent = username;
startQuizBtn.disabled = false;
startQuizBtn.textContent = "Start Quiz";

let timerInterval = null;
let activeQuestionId = null;
let answeredCurrentQuestion = false;

const socket = new WebSocket(`${protocol}://${window.location.host}/ws/quiz/${roomCode}/`);
refreshIdentity();

socket.onopen = function () {
    setConnectionState("Connected", "live");
    setStatus("Connected. Waiting for quiz events.");
};

socket.onclose = function () {
    setConnectionState("Disconnected", "err");
    setStatus("Connection lost. Refresh to reconnect.", true);
    startQuizBtn.disabled = true;
    disableOptions();
};

socket.onerror = function () {
    setConnectionState("Error", "err");
    setStatus("WebSocket error occurred.", true);
};

socket.onmessage = function (e) {
    const data = JSON.parse(e.data);

    if (data.type === "question") {
        showQuestion(data);
        startTimer(data.timer);
        return;
    }

    if (data.type === "leaderboard") {
        updateLeaderboard(data.data);
        return;
    }

    if (data.type === "question_closed") {
        disableOptions();
        setStatus("Time is up for this question.");
        timer.textContent = "Time: 0";
        return;
    }

    if (data.type === "quiz_finished") {
        clearTimer();
        disableOptions();
        questionBox.textContent = "Quiz finished. Final scores are on the leaderboard.";
        setStatus("Quiz completed.");
        startQuizBtn.disabled = true;
        return;
    }

    if (data.type === "error") {
        setStatus(data.message || "An error occurred.", true);
    }
};

function setConnectionState(text, typeClass) {
    connectionChip.textContent = text;
    connectionChip.className = "chip";
    if (typeClass) {
        connectionChip.classList.add(typeClass);
    }
}

function setStatus(message, isError = false) {
    statusText.textContent = message;
    statusText.className = isError ? "status error" : "status";
}

async function refreshIdentity() {
    if (!username || !roomCode) {
        return;
    }

    try {
        const response = await fetch("/api/quiz/join/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username,
                room_code: roomCode,
            }),
        });
        const data = await response.json();
        if (!response.ok) {
            return;
        }

        userId = Number.parseInt(String(data.player_id), 10);
        localStorage.setItem("user_id", String(userId));
    } catch (error) {
        // Keep existing local identity on failure.
    }
}

function startQuiz() {
    if (socket.readyState !== WebSocket.OPEN) {
        setStatus("Socket not connected yet.", true);
        return;
    }

    socket.send(JSON.stringify({ type: "start_quiz" }));
    setStatus("Quiz started.");
}

function showQuestion(data) {
    activeQuestionId = data.question_id;
    answeredCurrentQuestion = false;
    clearTimer();

    questionBox.textContent = data.text;
    optionsBox.innerHTML = "";

    data.options.forEach((option) => {
        const btn = document.createElement("button");
        btn.className = "option-btn";
        btn.type = "button";
        btn.textContent = option.text;
        btn.onclick = () => submitAnswer(data.question_id, option.id, btn);
        optionsBox.appendChild(btn);
    });

    setStatus("Question is live. Select one option.");
}

function submitAnswer(questionId, optionId, clickedButton) {
    if (!userId) {
        setStatus("Missing player identity. Rejoin from home page.", true);
        return;
    }

    if (answeredCurrentQuestion || questionId !== activeQuestionId) {
        return;
    }

    if (socket.readyState !== WebSocket.OPEN) {
        setStatus("Connection unavailable. Cannot submit answer.", true);
        return;
    }

    answeredCurrentQuestion = true;
    socket.send(
        JSON.stringify({
            type: "submit_answer",
            user_id: userId,
            question_id: questionId,
            option_id: optionId,
        })
    );

    Array.from(optionsBox.children).forEach((button) => {
        button.disabled = true;
        button.classList.remove("selected");
    });
    clickedButton.classList.add("selected");
    setStatus("Answer submitted.");
}

function disableOptions() {
    Array.from(optionsBox.children).forEach((button) => {
        button.disabled = true;
    });
}

function updateLeaderboard(data) {
    leaderboardBody.innerHTML = "";

    if (!data || data.length === 0) {
        leaderboardEmpty.style.display = "block";
        return;
    }

    leaderboardEmpty.style.display = "none";

    data.forEach((player, index) => {
        const row = document.createElement("tr");

        const rankCell = document.createElement("td");
        rankCell.textContent = String(index + 1);

        const nameCell = document.createElement("td");
        nameCell.textContent = player.player__username;
        if (player.player__username === username) {
            nameCell.classList.add("me");
        }

        const scoreCell = document.createElement("td");
        scoreCell.textContent = String(player.total_score || 0);

        row.appendChild(rankCell);
        row.appendChild(nameCell);
        row.appendChild(scoreCell);
        leaderboardBody.appendChild(row);
    });
}

function clearTimer() {
    if (timerInterval) {
        clearInterval(timerInterval);
        timerInterval = null;
    }
}

function startTimer(seconds) {
    let remaining = Number(seconds);
    clearTimer();

    if (Number.isNaN(remaining)) {
        timer.textContent = "Time: --";
        return;
    }

    timer.textContent = `Time: ${remaining}`;

    timerInterval = setInterval(() => {
        remaining -= 1;

        if (remaining <= 5 && remaining >= 0) {
            timer.style.color = "#b54708";
        } else {
            timer.style.color = "#165ca8";
        }

        timer.textContent = `Time: ${Math.max(remaining, 0)}`;

        if (remaining <= 0) {
            clearTimer();
        }
    }, 1000);
}

window.startQuiz = startQuiz;
