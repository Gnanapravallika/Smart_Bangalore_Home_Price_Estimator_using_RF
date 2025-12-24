async function predictPrice() {
    const location = document.getElementById("location").value.trim();
    const sqft = document.getElementById("sqft").value;
    const bhk = document.getElementById("bhk").value;
    const bath = document.getElementById("bath").value;

    const resultBox = document.getElementById("resultBox");
    const priceText = document.getElementById("priceText");

    // ---- Input validation ----
    if (!location || !sqft || !bhk || !bath) {
        alert("Please fill in all fields.");
        return;
    }

    if (sqft <= 0 || bhk <= 0 || bath <= 0) {
        alert("Values must be greater than zero.");
        return;
    }

    // ---- Loading state ----
    resultBox.style.display = "block";
    priceText.innerText = "⏳ Predicting price, please wait...";

    try {
        const response = await fetch("http://127.0.0.1:8000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                location: location,
                sqft: parseFloat(sqft),
                bhk: parseInt(bhk),
                bath: parseInt(bath)
            })
        });

        if (!response.ok) {
            throw new Error("API response error");
        }

        const data = await response.json();

        // ---- Business validation ----
        const price = Math.max(0, data.predicted_price_lakhs);

        // ---- Display result ----
        priceText.innerHTML = `
            <strong>₹ ${price} Lakhs</strong><br>
            <small>
                📍 Location: ${location}<br>
                📐 Area: ${sqft} sqft<br>
                🏠 BHK: ${bhk}, Bath: ${bath}
            </small>
        `;
    } catch (error) {
        console.error(error);
        priceText.innerHTML = `
            ❌ Unable to get prediction.<br>
            <small>Please ensure the backend server is running.</small>
        `;
    }
}
