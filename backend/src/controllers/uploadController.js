import axios from 'axios';
import dotenv from 'dotenv/config.js';

export const extractTextFromPDF = async (req, res) => {
    try {
	const URL =`${process.env.EXTRACT_TEXT_SERVICE_BASE_URL}/extract-data` 
	// excepts the filepath as query param
	
	const reponse = await axios.get(URL, {
		params:{ filePath: filePath}
	});
	res.status(200).json(response.data);
    } catch (error) {
	console.error("Error in extractTextFromPDF controller:", error)
        res.status(500).json({
            success: false,
            message: "Internal Server Error"
        });
   

    }
}
