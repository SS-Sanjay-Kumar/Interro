import express from 'express';
import {
    getVideoTranscript,
} from '../controllers/ytTranscriptController.js'

const router = express.Router();
// /yt-transcript
router.get("/:videoId", getVideoTranscript);

export default router;