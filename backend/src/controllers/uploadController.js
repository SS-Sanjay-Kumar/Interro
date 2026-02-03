import axios from 'axios';
import dotenv from 'dotenv/config.js';
import fs from 'fs/promises';

export const extractTextFromPDF = async (req, res) => {
    try {
	const URL =`${process.env.EXTRACT_TEXT_SERVICE_BASE_URL}/extract-data` 
	// excepts the filepath as query param
	const filePath = "sample.pdf"; //hardcoded for testing purposes		
	console.log(URL, filePath);
	const response = await axios.get(URL, {
		params:{ filePath: filePath}
	});
	// after file is processed, delete the file
	await fs.unlink(`../uploads/${filePath}`); //filePath is essentially just the file name, so refactor the code to improve its quality
	res.status(200).json(response.data);
    } catch (error) {
	console.error("Error in extractTextFromPDF controller:", error)
        res.status(500).json({
            success: false,
            message: "Internal Server Error"
        });
   

    }
}
