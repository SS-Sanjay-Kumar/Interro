import { useState } from "react";
import { uploadFile } from "../api/uploads";

export default function FileUploadCard({ onUploaded }) {
    const [file, setFile] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState("");

    async function handleUpload() {
        if (!file) return;

        setLoading(true);
        setError("");

        try {
            const res = await uploadFile(file);
            onUploaded(res.fileName);
        } catch (err) {
            setError(err.message);
        } finally {
            setLoading(false);
        }
    }

    return (
        <div className="card bg-base-100 border border-base-300 shadow mb-6">
            <div className="card-body">
                <h2 className="card-title">Upload Study Material</h2>

                <input
                    type="file"
                    className="file-input file-input-bordered w-full"
                    onChange={(e) => setFile(e.target.files[0])}
                />

                <button
                    className={`btn btn-primary mt-4 ${loading ? "loading" : ""}`}
                    onClick={handleUpload}
                    disabled={!file}
                >
                    Upload
                </button>

                {error && (
                    <div className="alert alert-error mt-4">
                        <span>{error}</span>
                    </div>
                )}
            </div>
        </div>
    );
}
