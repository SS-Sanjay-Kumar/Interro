import axios from 'axios'
import dotenv from 'dotenv/config.js'

export const getVideoTranscript = async (req, res) => {
    try {
        const videoId = req.params.videoId;
        const URL = `${process.env.YT_TRANSCRIPT_SERVICE_BASE_URL}/yt-transcript-service/${videoId}`

        const response = await axios.get(URL);
        return res.status(200).json(response.data);

    } catch (error) {
        console.error("Error in getVideoTranscript controller:", error);
        return res.status(500).json({ message: "Internal Server Error" });
    }
}