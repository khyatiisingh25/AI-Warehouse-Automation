# AI Pipeline
## Overview

The AI Pipeline defines how AI models interact with the backend, frontend, and database.

Instead of embedding AI logic directly into the application, each AI model is treated as an independent module that receives input, performs inference, and returns structured results to the FastAPI backend.

This modular design makes the system scalable and allows AI models to be upgraded without affecting the rest of the application.
## AI Modules

1. Product Detection (YOLOv8)
2. Shelf Occupancy Detection
3. Demand Prediction
4. Route Optimization
5. Alert Generation
Camera / Image Upload
        │
        ▼
FastAPI Detection API
        │
        ▼
YOLOv8 Inference
        │
        ▼
Detection Results
        │
        ├────────► PostgreSQL
        │
        ▼
Analytics Dashboard
