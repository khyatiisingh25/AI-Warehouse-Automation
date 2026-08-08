# System Architecture

## Overview

The AI-Based Warehouse Automation & Digital Twin System follows a modular, layered architecture designed for scalability, maintainability, and easy integration.

Each component has a single responsibility and communicates through well-defined REST APIs. This allows different team members to work on independent modules while ensuring that all parts integrate smoothly.

The FastAPI backend acts as the central communication layer between the frontend, AI modules, Machine Learning models, Digital Twin, and PostgreSQL database.

---

## Architecture Layers

The system consists of five major layers:

1. Frontend Layer
2. Backend Layer
3. AI Layer (Computer Vision)
4. Machine Learning Layer
5. Database Layer

---

## Overall System Flow

```text
                    User
                      │
                      ▼
        React + Tailwind CSS Frontend
                      │
             REST API Requests
                      │
                      ▼
             FastAPI Backend Server
        ┌─────────┼──────────┬──────────┐
        │         │          │          │
        ▼         ▼          ▼          ▼
 PostgreSQL   AI Engine   ML Engine  Digital Twin
        │         │          │
        └─────────┴──────────┘
                  │
                  ▼
            JSON Response
                  │
                  ▼
        React Dashboard
```

---

# System Components

## 1. Frontend Layer

### Responsibilities

- User Interface
- Dashboard
- Warehouse Visualization
- Analytics Charts
- Voice Assistant Interface
- Sending API Requests
- Displaying AI Results

### Technology

- React
- Tailwind CSS

---

## 2. Backend Layer

### Responsibilities

- REST APIs
- Business Logic
- Authentication
- Authorization
- AI Integration
- ML Integration
- Database Communication
- Digital Twin Communication
- Request Validation
- Response Generation

### Technology

- FastAPI
- Python

---

## 3. AI Layer (Computer Vision)

### Responsibilities

- Product Detection using YOLOv8
- Shelf Occupancy Detection
- Image Processing
- Object Recognition
- AI Inference

### Technology

- Python
- YOLOv8
- OpenCV

---

## 4. Machine Learning Layer

### Responsibilities

- Demand Prediction
- Sales Forecasting
- Inventory Trend Analysis
- Prediction Generation

### Technology

- Python
- Scikit-learn
- Pandas

---

## 5. Database Layer

### Responsibilities

- Store Products
- Store Inventory
- Store Shelf Information
- Store Users
- Store AI Predictions
- Store Detection Logs
- Store Alerts
- Store System Logs

### Technology

- PostgreSQL

---

# Communication Flow

The communication between components follows this sequence:

1. The user interacts with the React frontend.
2. The frontend sends REST API requests to the FastAPI backend.
3. The backend validates the request.
4. Depending on the request, the backend:
   - Reads or writes data in PostgreSQL.
   - Calls the AI Engine for product detection.
   - Calls the Machine Learning Engine for demand prediction.
   - Communicates with the Digital Twin module for warehouse simulation.
5. The backend combines all results into a structured JSON response.
6. The frontend displays the results to the user.

---

# Design Principles

The architecture follows these principles:

- Modular Design
- Separation of Concerns
- Scalability
- Maintainability
- Loose Coupling
- High Cohesion
- RESTful Communication
- Reusable Components

---

# Benefits of the Architecture

- Easy to maintain
- Easy to extend with new modules
- Independent development by multiple team members
- Simplified testing
- Clear separation of responsibilities
- Supports future deployment using Docker
- Suitable for production-style development