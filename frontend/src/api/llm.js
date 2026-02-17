const BASE_URL = "http://localhost:8000/api/v1";

export async function fetchQuizFromBackend(payload) {
    const res = await fetch(`${BASE_URL}/llm-call`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
    });

    if (!res.ok) {
        const error = await res.json();
        throw new Error(error.detail || "Failed to generate quiz");
    }

    return res.json();
}
