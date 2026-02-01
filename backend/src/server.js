import express from 'express';
import dotenv from 'dotenv/config.js';

import transcriptRoutes from './routes/transcriptRoutes.js';
import uploadRoutes from './routes/uploadRoutes.js';
import resourceRoutes from './routes/resourceRoutes.js'

const app = express();
const PORT = process.env.PORT;

// * MIDDLEWARES
app.use(express.json());

// * ROUTES
app.get("/api/health", (req, res) => {
    res.json({ project: "Interro", status: "ok" });
});

// route for transcribing yt videos
app.use("/api/transcript", transcriptRoutes);
app.use("/api/upload", uploadRoutes);
app.use("/api/resource", resourceRoutes);

// todo: implement auto delete files after extracting content

app.listen(PORT, () => {
    console.log("Server running at port", PORT);
})