# Team Module Specifications

This document defines the ownership, responsibilities, dependencies, and deliverables for each team member.

Each member owns their primary module but must follow the common project architecture and API contracts.
# 1. Khyati

## Role

Team Leader & Lead AI Systems Engineer

## Responsibilities

- Overall System Architecture
- Folder Structure
- API Design
- AI Integration
- Backend ↔ AI Communication
- Frontend ↔ Backend Integration
- AI Inference Pipeline
- GitHub Workflow
- Code Reviews
- Merge Requests
- Documentation
- Performance Optimization
- Integration Testing

## Primary Folders

backend/

ai/

docs/

## Dependencies

Works with every module.

Responsible for integrating the entire system.
# 2. Ayush

## Role

Backend Engineer

## Responsibilities

- FastAPI
- PostgreSQL
- Authentication
- CRUD APIs
- Database Optimization
- Backend Testing

## Primary Folder

backend/

## Depends On

API Design

Database Design

Works Closely With

Khyati
# 3. Anjali

## Role

Frontend Engineer

## Responsibilities

- React
- Dashboard
- Charts
- Responsive UI
- API Integration
- Warehouse Visualization

## Primary Folder

frontend/

## Depends On

Backend APIs

Works Closely With

Ayush

Khyati
# 4. Shubham

## Role

Machine Learning Engineer

## Responsibilities

- Dataset Collection
- Data Cleaning
- Demand Prediction
- Model Evaluation
- Model Improvement

## Primary Folder

ai/

## Depends On

Dataset

Works Closely With

Khyati
# 5. Anshul

## Role

Simulation & DevOps Engineer

## Responsibilities

- Digital Twin
- Path Optimization
- Docker
- Deployment
- System Testing

## Primary Folder

docker/

## Depends On

Backend APIs

Works Closely With

Khyati
