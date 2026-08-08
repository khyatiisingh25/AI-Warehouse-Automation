# Database Design

## Database

PostgreSQL

---

## Main Tables

1. Users
2. Products
3. Inventory
4. Shelves
5. Detections
6. Predictions
7. Alerts
8. Activity Logs

---

## Table Relationships

Users
│
├── manages Inventory
│
├── manages Shelves
│
└── receives Alerts

Products
│
└── stored inside Inventory

Inventory
│
└── assigned to Shelves

Shelves
│
└── monitored by AI Detection

Detections
│
├── update Inventory
└── generate Alerts

Predictions
│
└── generated from historical Inventory data

Alerts
│
└── linked to Products or Shelves

Activity Logs
│
└── store important system events