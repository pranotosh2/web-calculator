let display = document.getElementById("display");

function append(value) {
    if (display.value === "Invalid" || display.value.startsWith("Error")) {
        display.value = "";
    }
    display.value += value;
}

function clearDisplay() {
    display.value = "";
}

function backspace() {
    if (display.value === "Invalid" || display.value.startsWith("Error")) {
        display.value = "";
    } else {
        display.value = display.value.slice(0, -1);
    }
}

async function calculate() {
    let expression = display.value.trim();
    if (!expression) return;

    // Dynamic backend location depending on whether page is served via HTTP or direct file load
    const apiBase = window.location.protocol === 'file:' ? 'http://127.0.0.1:8000' : '';

    try {
        const response = await fetch(
            `${apiBase}/calculate`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    expression: expression
                })
            }
        );

        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }

        const data = await response.json();
        display.value = data.result;
    } catch (err) {
        display.value = "Error: Connection failed";
    }
}