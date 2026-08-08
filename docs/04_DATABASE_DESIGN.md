# Database Design
## Overview

The project uses PostgreSQL as the primary relational database.

The database stores all warehouse information including products, inventory, shelves, users, AI predictions, alerts, and system logs.

The database is designed using normalization principles to minimize redundancy while maintaining efficient query performance.
## Main Tables

1. Users
2. Products
3. Inventory
4. Shelves
5. Shelf Occupancy
6. Orders
7. Demand Predictions
8. Alerts
9. Detection Logs
10. Activity Logs
## Entity Relationships

- One User can manage multiple Inventory records.
- One Product can exist in multiple Inventory records.
- One Shelf can store multiple Products.
- One Product can have multiple Demand Predictions.
- One Product can generate multiple Detection Logs.
- One Inventory record belongs to one Shelf.
- Alerts can be generated for Inventory, Shelves, or AI Predictions.
# Users Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| user_id | UUID | Primary Key | Unique identifier for each user |
| full_name | VARCHAR(100) | NOT NULL | Full name of the user |
| email | VARCHAR(255) | UNIQUE, NOT NULL | User email address |
| password_hash | VARCHAR(255) | NOT NULL | Encrypted password |
| role | VARCHAR(50) | NOT NULL | Admin, Manager, Operator |
| phone_number | VARCHAR(20) | NULL | Contact number |
| is_active | BOOLEAN | DEFAULT TRUE | Whether the account is active |
| created_at | TIMESTAMP | NOT NULL | Account creation time |
| updated_at | TIMESTAMP | NOT NULL | Last profile update |
# Products Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| product_id | UUID | Primary Key | Unique product identifier |
| sku | VARCHAR(50) | UNIQUE, NOT NULL | Stock Keeping Unit |
| product_name | VARCHAR(255) | NOT NULL | Product name |
| category | VARCHAR(100) | NOT NULL | Product category |
| brand | VARCHAR(100) | NULL | Product brand |
| description | TEXT | NULL | Product description |
| unit_price | DECIMAL(10,2) | NOT NULL | Selling price |
| weight | DECIMAL(10,2) | NULL | Product weight |
| barcode | VARCHAR(100) | UNIQUE | Product barcode |
| created_at | TIMESTAMP | NOT NULL | Product creation time |
| updated_at | TIMESTAMP | NOT NULL | Last update time |
# Shelves Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| shelf_id | UUID | Primary Key | Unique shelf identifier |
| shelf_code | VARCHAR(50) | UNIQUE, NOT NULL | Shelf code (e.g., A-01-03) |
| zone | VARCHAR(50) | NOT NULL | Warehouse zone |
| rack | VARCHAR(50) | NOT NULL | Rack number |
| level | INTEGER | NOT NULL | Shelf level |
| max_capacity | INTEGER | NOT NULL | Maximum storage capacity |
| current_capacity | INTEGER | DEFAULT 0 | Current occupied capacity |
| status | VARCHAR(20) | DEFAULT 'Available' | Available, Full, Maintenance |
| created_at | TIMESTAMP | NOT NULL | Record creation time |
| updated_at | TIMESTAMP | NOT NULL | Last update time |
# Inventory Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| inventory_id | UUID | Primary Key | Unique inventory record |
| product_id | UUID | Foreign Key | References Products table |
| shelf_id | UUID | Foreign Key | References Shelves table |
| quantity | INTEGER | NOT NULL | Available quantity |
| minimum_stock | INTEGER | DEFAULT 10 | Minimum stock threshold |
| last_updated | TIMESTAMP | NOT NULL | Last inventory update |
# Detection Logs Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| detection_id | UUID | Primary Key | Unique detection record |
| product_id | UUID | Foreign Key | Detected product |
| confidence_score | DECIMAL(5,2) | NOT NULL | AI confidence percentage |
| image_path | TEXT | NOT NULL | Uploaded image location |
| detected_at | TIMESTAMP | NOT NULL | Detection timestamp |
# Demand Predictions Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| prediction_id | UUID | Primary Key | Unique prediction record |
| product_id | UUID | Foreign Key | References Products table |
| predicted_quantity | INTEGER | NOT NULL | Predicted future demand |
| prediction_date | DATE | NOT NULL | Date for which demand is predicted |
| model_version | VARCHAR(50) | NOT NULL | ML model version |
| created_at | TIMESTAMP | NOT NULL | Prediction generation time |
# Alerts Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| alert_id | UUID | Primary Key | Unique alert identifier |
| title | VARCHAR(255) | NOT NULL | Alert title |
| message | TEXT | NOT NULL | Alert description |
| alert_type | VARCHAR(50) | NOT NULL | Low Stock, Detection, Prediction, System |
| priority | VARCHAR(20) | NOT NULL | Low, Medium, High |
| is_read | BOOLEAN | DEFAULT FALSE | Alert read status |
| created_at | TIMESTAMP | NOT NULL | Alert creation time |
# Activity Logs Table

| Column Name | Data Type | Constraints | Description |
|-------------|----------|------------|-------------|
| log_id | UUID | Primary Key | Unique log identifier |
| user_id | UUID | Foreign Key | User who performed the action |
| action | VARCHAR(255) | NOT NULL | Action performed |
| module | VARCHAR(100) | NOT NULL | Module where action occurred |
| created_at | TIMESTAMP | NOT NULL | Action timestamp |
