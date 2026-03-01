function getCookie(name) {
    const value = `; ${document.cookie}`;
    const parts = value.split(`; ${name}=`);
    if (parts.length === 2) {
        return parts.pop().split(";").shift();
    }
    return "";
}

async function loadCategories() {
    const categorySelect = document.getElementById("category");
    categorySelect.innerHTML = "<option value=''>Loading categories...</option>";

    try {
        const response = await fetch("/api/quiz/categories/");
        const data = await response.json();

        if (!response.ok || !Array.isArray(data.categories)) {
            throw new Error(data.error || "Unable to load categories.");
        }

        categorySelect.innerHTML = "";
        data.categories.forEach((category) => {
            const option = document.createElement("option");
            option.value = category.key;
            option.textContent = `${category.name} (${category.amount} questions)`;
            categorySelect.appendChild(option);
        });
    } catch (error) {
        categorySelect.innerHTML = "<option value='gk'>General Knowledge</option>";
    }
}

async function joinRoom() {
    const usernameInput = document.getElementById("username");
    const categoryInput = document.getElementById("category");
    const roomCodeInput = document.getElementById("roomCode");
    const joinBtn = document.getElementById("joinBtn");
    const message = document.getElementById("message");

    const username = usernameInput.value.trim();
    const category = categoryInput.value;
    const roomCode = roomCodeInput.value.trim().toUpperCase();

    message.className = "message";
    message.textContent = "";

    if (!username) {
        message.className = "message error";
        message.textContent = "Username is required.";
        return;
    }

    if (!roomCode && !category) {
        message.className = "message error";
        message.textContent = "Select a category or enter a room code.";
        return;
    }

    joinBtn.disabled = true;
    joinBtn.textContent = "Joining...";

    const payload = {
        username,
    };
    if (roomCode) {
        payload.room_code = roomCode;
    } else {
        payload.category = category;
    }

    try {
        const response = await fetch("/api/quiz/join/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken")
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.error || "Unable to join quiz.");
        }

        localStorage.setItem("username", username);
        localStorage.setItem("user_id", String(data.player_id));
        localStorage.setItem("room_code", data.room_code);
        localStorage.setItem("category", data.category || category || "gk");
        window.location.href = `/room/${data.room_code}/`;
    } catch (error) {
        message.className = "message error";
        message.textContent = error.message;
    } finally {
        joinBtn.disabled = false;
        joinBtn.textContent = "Create/Join Room";
    }
}

loadCategories();
window.joinRoom = joinRoom;
