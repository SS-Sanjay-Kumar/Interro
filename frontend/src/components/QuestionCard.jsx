export default function QuestionCard({ qKey, questionData, onAnswer }) {
    const { question, options, marks } = questionData;

    return (
        <div className="card bg-base-100 border border-base-300 shadow-sm hover:shadow transition mb-4">

            <div className="card-body">
                <h3 className="font-semibold mb-2">
                    {qKey.toUpperCase()}: {question}
                </h3>

                <div className="space-y-2">
                    {Object.entries(options).map(([key, value]) => (
                        <label key={key} className="flex items-center gap-2 cursor-pointer">
                            <input
                                type="radio"
                                name={qKey}
                                className="radio radio-primary"
                                onChange={() => onAnswer(qKey, key)}
                            />
                            <span>
                                <b>{key.toUpperCase()}.</b> {value}
                            </span>
                        </label>
                    ))}
                </div>

                <p className="text-xs opacity-60 mt-3">Marks: {marks}</p>
            </div>
        </div>
    );
}
