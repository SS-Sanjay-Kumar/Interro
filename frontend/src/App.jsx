import { useState } from "react";
import Navbar from "./components/Navbar";
import Quiz from "./components/Quiz";
import StudyInputCard from "./components/StudyInputCard";
import { fetchQuizFromBackend } from "./api/llm";

export default function App() {
  const [quizData, setQuizData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleGenerate(payload) {
    setLoading(true);
    setError("");
    setQuizData(null);

    try {
      const data = await fetchQuizFromBackend(payload);
      setQuizData(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-base-200">
      <Navbar />

      <div className="max-w-3xl mx-auto p-6">
        <StudyInputCard onReady={handleGenerate} />

        {loading && (
          <div className="flex justify-center mt-10">
            <span className="loading loading-spinner loading-lg"></span>
          </div>
        )}

        {error && (
          <div className="alert alert-error mt-6">
            <span>{error}</span>
          </div>
        )}

        {quizData && <Quiz data={quizData} />}
      </div>
    </div>
  );
}
