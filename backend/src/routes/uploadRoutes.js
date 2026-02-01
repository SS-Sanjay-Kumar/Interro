import express from "express";
import { fileUploader } from "../middleware/multer.middleware.js";

const router = express.Router();

// fileUploader.single("file") -> This tells Multer:
// * Look for a multipart form field called file.
// * Parse it. Save it to disk. Attach metadata to req.file.

router.post("/", fileUploader.single("file"), (req, res) => {
    if (!req.file) {
        return res.status(400).json({
            success: false,
            message: "No file uploaded",
        });
    }

    return res.status(200).json({
        success: true,
        message: "File uploaded successfully",
        filePath: req.file.path,
    });
}
);

export default router;
