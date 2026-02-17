const BASE_URL = "http://localhost:8000/api/v1";

export async function uploadFile(file) {
    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch(`${BASE_URL}/uploads/upload-file`, {
        method: "POST",
        body: formData,
    });

    if (!res.ok) {
        const err = await res.json();
        throw new Error(err.message || "Upload failed");
    }

    return res.json(); // { fileName: "..." }
}
