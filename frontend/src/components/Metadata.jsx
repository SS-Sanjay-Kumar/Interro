export default function Metadata({ metadata }) {
    return (

        <div className="card bg-base-100 border border-base-300 shadow-sm hover:shadow transition mb-4">

            <div className="card-body">
                <h2 className="card-title">Test Overview</h2>

                <div className="grid grid-cols-2 gap-4 text-sm">
                    <p><b>Topic:</b> {metadata.topic}</p>
                    <p><b>Questions:</b> {metadata.no_of_questions}</p>
                    <p><b>Total Marks:</b> {metadata.total_marks}</p>
                    <p><b>Minimum to Pass:</b> {metadata.minimum_marks}</p>
                </div>

                {metadata.message && (
                    <div className="alert alert-warning mt-4">
                        <span>{metadata.message}</span>
                    </div>
                )}
            </div>
        </div>
    );
}
