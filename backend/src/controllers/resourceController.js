import axios from 'axios'

export const getResourceByUrl = async (req, res) => {
    try {
        const resourceURL = req.query.resourceUrl;
        const URL = `${process.env.URL_INGEST_SERVICE_BASE_URL}/url-ingest`;

        const response = await axios.get(URL, {
            params: { resourceURL: resourceURL }
        });
        res.status(200).json(response.data)
    } catch (error) {
        console.error("Error in getResourceByUrl controller:", error)
        res.status(500).json({
            success: false,
            message: "Internal Server Error"
        });
    }
}