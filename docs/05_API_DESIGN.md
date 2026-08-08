# API Design

## Overview

The backend exposes RESTful APIs that allow communication between the frontend, AI modules, database, and external services.

Each API follows standard HTTP methods and returns JSON responses.
## API Version

Base URL

/api/v1/
## API Modules

| Module | Purpose |
|---------|---------|
| Users | Authentication & User Management |
| Inventory | Inventory CRUD Operations |
| Detection | Product Detection using YOLOv8 |
| Shelves | Shelf Occupancy |
| Prediction | Demand Prediction |
| Optimization | Picking Route & Slot Optimization |
| Analytics | Dashboard Data |
| Alerts | Notifications |
| Voice | Voice Assistant |
## HTTP Methods

GET → Retrieve Data

POST → Create Resource

PUT → Update Resource

DELETE → Remove Resource
## Planned Endpoints
## API Documentation Format

Each API endpoint includes:

- Endpoint URL
- HTTP Method
- Purpose
- Request Body
- Success Response
- Error Responses
- Authentication Required
- Database Tables Used
- Module Owner
# Authentication APIs

---

## Login

**Endpoint**

POST /api/v1/users/login

**Purpose**

Authenticate a user and generate an access token.

**Request Body**

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

**Success Response**

```json
{
  "access_token": "jwt_token",
  "token_type": "Bearer"
}
```

**Authentication Required**

No

**Database Tables**

Users

**Owner**

Ayush
---

## Get User Profile

**Endpoint**

GET /api/v1/users/profile

**Purpose**

Retrieve logged-in user information.

**Authentication Required**

Yes

**Database Tables**

Users

**Owner**

Ayush
# API Endpoints

## Authentication

POST   /api/v1/users/login
GET    /api/v1/users/profile

---

## Inventory

GET    /api/v1/inventory
GET    /api/v1/inventory/{id}
POST   /api/v1/inventory
PUT    /api/v1/inventory/{id}
DELETE /api/v1/inventory/{id}

---

## Products

GET    /api/v1/products
GET    /api/v1/products/{id}
POST   /api/v1/products
PUT    /api/v1/products/{id}
DELETE /api/v1/products/{id}

---

## Shelves

GET    /api/v1/shelves
GET    /api/v1/shelves/{id}
PUT    /api/v1/shelves/{id}

---

## Detection

POST   /api/v1/detection/detect
GET    /api/v1/detection/history

---

## Predictions

POST   /api/v1/predictions/generate
GET    /api/v1/predictions

---

## Analytics

GET    /api/v1/analytics/dashboard

---

## Alerts

GET    /api/v1/alerts
PUT    /api/v1/alerts/{id}/read

---

## Voice

POST   /api/v1/voice/query
