const form = document.getElementById("prediction-form");
const resultDiv = document.getElementById("result");
const clearBtn = document.getElementById("clear-btn");

// Handle prediction
form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const data = Object.fromEntries(formData.entries());

    try {
        const response = await fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        // Handle backend error
        if (result.error) {
            resultDiv.innerHTML = `<span style="color:red">${result.error}</span>`;
            return;
        }

        // format price
        const formattedPrice = Number(result.prediction).toLocaleString(undefined, {
            minimumFractionDigits: 2,
            maximumFractionDigits: 2
        });

        resultDiv.innerHTML = `<strong>Predicted Price:</strong> $${formattedPrice}`;

    } catch (error) {
        resultDiv.innerHTML = "Error connecting to server";
    }
});

// Handle clear
clearBtn.addEventListener("click", () => {
    form.reset();
    resultDiv.innerHTML = "Result will appear here";
});