import { useState } from "react";
import { uploadFile } from "../api/uploads";

export default function StudyInputCard({ onReady }) {
    const [url, setUrl] = useState("");
    const [youtube, setYoutube] = useState("");
    const [file, setFile] = useState(null);
    const [fileName, setFileName] = useState(null);
    const [uploading, setUploading] = useState(false);
    const [error, setError] = useState("");

    async function handleFileUpload() {
        if (!file) return;

        setUploading(true);
        setError("");

        try {
            const res = await uploadFile(file);
            setFileName(res.fileName);
        } catch (err) {
            setError(err.message);
        } finally {
            setUploading(false);
        }
    }

    function handleContinue() {
        if (!url && !youtube && !fileName) {
            setError("Please provide at least one study material.");
            return;
        }
        onReady({
            fileName: fileName || null,
            resourceURL: url || null,
            ytVideoId: youtube || null,
        });

    }

    return (
        <div className="card bg-base-100 border border-base-300 shadow mb-6">
            <div className="card-body space-y-4">
                <h2 className="card-title">Provide Study Material</h2>
                <p className="text-sm opacity-70">
                    Enter at least one source below
                </p>

                {/* Resource URL */}
                <input
                    type="url"
                    placeholder="Enter resource link (article / blog)"
                    className="input input-bordered w-full"
                    value={url}
                    onChange={(e) => setUrl(e.target.value)}
                />

                {/* YouTube URL */}
                <input
                    type="text"
                    placeholder="Enter YouTube video link or ID"
                    className="input input-bordered w-full"
                    value={youtube}
                    onChange={(e) => setYoutube(e.target.value)}
                />

                {/* File Upload */}
                <div className="flex gap-2">
                    <input
                        type="file"
                        className="file-input file-input-bordered w-full"
                        onChange={(e) => setFile(e.target.files[0])}
                    />

                    <button
                        className={`btn btn-outline ${uploading ? "loading" : ""}`}
                        onClick={handleFileUpload}
                        disabled={!file}
                    >
                        Upload
                    </button>
                </div>

                {fileName && (
                    <div className="alert alert-success">
                        <span>Uploaded: {fileName}</span>
                    </div>
                )}

                {error && (
                    <div className="alert alert-error">
                        <span>{error}</span>
                    </div>
                )}

                <button
                    className="btn btn-primary w-full mt-2"
                    onClick={handleContinue}
                >
                    Generate Test
                </button>
            </div>
        </div>
    );
}
