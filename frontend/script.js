
const API_URL =
    "https://sncf1wb3h7.execute-api.us-east-1.amazonaws.com/dev";

const form = document.getElementById("complaintForm");
const submitMessage = document.getElementById("submitMessage");
const submitButton = document.getElementById("submitButton");

const trackButton = document.getElementById("trackButton");
const trackingResult = document.getElementById("trackingResult");


// Register a complaint
form.addEventListener("submit", async function (event) {
    event.preventDefault();

    const complaint = {
        name: document.getElementById("name").value.trim(),
        phone: document.getElementById("phone").value.trim(),
        category: document.getElementById("category").value,
        location: document.getElementById("location").value.trim(),
        description: document.getElementById("description").value.trim()
    };

    submitMessage.textContent = "Submitting complaint...";
    submitButton.disabled = true;

    try {
        const response = await fetch(`${API_URL}/complaints`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(complaint)
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.message || "Complaint submission failed"
            );
        }

        submitMessage.textContent =
            "Complaint registered successfully! Your ID: " +
            result.complaintId;

        document.getElementById("trackId").value =
            result.complaintId;

        form.reset();

    } catch (error) {
        submitMessage.textContent = error.message;
    } finally {
        submitButton.disabled = false;
    }
});


// Track a complaint
trackButton.addEventListener("click", async function () {
    const complaintId =
        document.getElementById("trackId").value.trim();

    if (!complaintId) {
        trackingResult.textContent =
            "Please enter your complaint ID.";
        return;
    }

    trackingResult.textContent = "Checking complaint...";
    trackButton.disabled = true;

    try {
        const response = await fetch(
            `${API_URL}/complaints/${encodeURIComponent(complaintId)}`
        );

        const result = await response.json();

        if (!response.ok) {
            throw new Error(
                result.message || "Complaint not found"
            );
        }

        trackingResult.textContent =
            "Complaint ID: " + result.complaintId + "\n" +
            "Category: " + result.category + "\n" +
            "Status: " + result.status;

    } catch (error) {
        trackingResult.textContent = error.message;
    } finally {
        trackButton.disabled = false;
    }
});
