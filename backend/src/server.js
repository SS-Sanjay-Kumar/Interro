import express from 'express';
import dotenv from 'dotenv/config.js';
const app = express();

const PORT = process.env.PORT;

app.get("/health", (req, res) => {
    res.json({ project: "Interro", status: "ok" });
});

app.listen(PORT, () => {
    console.log("Server running at port", PORT);
})