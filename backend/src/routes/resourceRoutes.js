import express from 'express';
import axios from 'axios';
import dotenv from 'dotenv/config.js';
import { getResourceByUrl } from '../controllers/resourceController.js';

const router = express.Router();

// /api/resource
router.get("/", getResourceByUrl);

export default router;

