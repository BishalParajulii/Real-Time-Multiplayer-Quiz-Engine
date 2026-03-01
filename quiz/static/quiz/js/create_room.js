function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(";").shift();
    }
    return "";
}

async function createRoom() {
    const hostInput = document.getElementById("hostName");
    const titleInput = document.getElementById("quizTitle");
    const createBtn = document.getElementById("createBtn");
    const message = document.getElementById("message");
    const resultBox = document.getElementById("resultBox");
    const roomCodeText = document.getElementById("createdRoomCode");

    const username = hostInput.value.trim();
    const title = titleInput.value.trim();

    message.className = "message";
    message.textContent = "";
    resultBox.style.display = "none";

    if (!username || !title) {
        message.className = "message error";
        message.textContent = "Host name and quiz title are required.";
        return;
    }

    createBtn.disabled = true;
    createBtn.textContent = "Creating...";

    try {
        const response = await fetch("/api/quiz/create/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify({ username, title })
        });

        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.error || "Failed to create quiz room.");
        }

        localStorage.setItem("username", username);
        localStorage.setItem("user_id", String(data.host_id));
        localStorage.setItem("host_id", String(data.host_id));
        localStorage.setItem("room_code", data.room_code);

        roomCodeText.textContent = data.room_code;
        resultBox.style.display = "block";
        message.textContent = "Quiz room created. Add questions from admin, then join room.";
    } catch (error) {
        message.className = "message error";
        message.textContent = error.message;
    } finally {
        createBtn.disabled = false;
        createBtn.textContent = "Create Room";
    }
}

window.createRoom = createRoom;
