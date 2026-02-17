import { useState } from "react";
import Metadata from "./Metadata";
import QuestionCard from "./QuestionCard";

export default function Quiz({ data }) {
    const [answers, setAnswers] = useState({});

    const { metadata, ...questions } = data;

    function handleAnswer(questionKey, optionKey) {
        setAnswers((prev) => ({
            ...prev,
            [questionKey]: optionKey,
        }));
    }

    function handleSubmit() {
        console.log("User answers:", answers);
        alert("Test submitted! (evaluation comes later)");
    }

    return (

        <div className="min-h-screen bg-base-200 py-8">
            <div className="max-w-3xl mx-auto px-6">

                <Metadata metadata={metadata} />

                {Object.entries(questions).map(([key, value]) => (
                    <QuestionCard
                        key={key}
                        qKey={key}
                        questionData={value}
                        onAnswer={handleAnswer}
                    />
                ))}

                <button className="btn btn-primary w-full mt-6" onClick={handleSubmit}>
                    Submit Test
                </button>
            </div>
        </div>
    );
}
