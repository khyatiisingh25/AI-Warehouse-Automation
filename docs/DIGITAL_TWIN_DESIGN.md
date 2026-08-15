# Digital Twin Design

## 1. Purpose

The Digital Twin represents the warehouse physical/simulated environment.

It will use warehouse state from the backend and provide the simulation layer for robot movement, pathfinding, and warehouse state visualization.

The Digital Twin should not create a second unrelated database model system.

---

## 2. Entity Overview

### Backend-connected entities

These entities already exist in the backend:

- Product
- Shelf
- Inventory
- Alert

### Digital Twin / Simulation entities

These entities are used by the simulation:

- Warehouse
- Zone
- Bin
- Robot / AGV
- Order

Some entities may overlap conceptually with backend entities, but simulation-specific state should remain separate from the backend database schema.

---

## 3. Backend Entity Mapping

### Product

Backend fields:

- product_id
- sku
- product_name
- category
- brand
- description
- unit_price
- weight
- barcode
- created_at
- updated_at

Digital Twin uses Product mainly to identify and represent products stored or moved inside the warehouse.

---

### Shelf

Backend fields:

- shelf_id
- shelf_code
- zone
- rack
- level
- max_capacity
- current_capacity
- status
- created_at
- updated_at

The Digital Twin may additionally maintain a simulation-specific grid position for pathfinding.

The simulation position should not be treated as a backend database field.

---

### Inventory

Backend fields:

- inventory_id
- product_id
- shelf_id
- quantity
- minimum_stock
- last_updated

Important:

product_id and shelf_id are the current backend relationships.

The Digital Twin must not assume bin_id as a backend inventory relationship.

---

### Alert

Backend fields:

- alert_id
- title
- message
- alert_type
- priority
- is_read
- created_at

Alerts can represent warehouse events or conditions that need attention.

---

## 4. Digital Twin Simulation Entities

### Warehouse

Purpose:

Represents the complete simulated warehouse environment.

Fields:

- warehouse_id
- rows
- columns
- layout

---

### Zone

Purpose:

Represents a logical area of the warehouse.

Fields:

- zone_id
- name
- zone_type
- boundary

The current backend Shelf model stores a zone value.

A separate backend Zone model has not been confirmed yet.

---

### Bin

Purpose:

Represents a simulation-level storage subdivision inside a shelf.

Fields:

- bin_id
- shelf_id
- position
- capacity
- status

Bin is currently a Digital Twin simulation concept.

It should not be treated as a backend database entity until a backend contract is defined.

---

### Robot / AGV

Purpose:

Represents a warehouse robot or automated guided vehicle in the simulation.

Fields:

- robot_id
- current_position
- target_position
- current_route
- battery_level
- state

Possible states:

- IDLE
- MOVING
- WAITING
- BLOCKED
- COMPLETED

Robot / AGV is currently a simulation entity.

No backend Robot model has been confirmed yet.

---

### Order

Purpose:

Represents a warehouse movement/picking task in the simulation.

Fields:

- order_id
- items
- priority
- source
- destination
- state

Possible states:

- CREATED
- PENDING
- IN_PROGRESS
- COMPLETED
- CANCELLED

A backend Order model has not been confirmed yet, so this remains a simulation-level concept for now.

---

## 5. Backend → Digital Twin Data Flow

    Frontend
        |
        | REST API
        v
    FastAPI Backend
        |
        | Warehouse state / tasks
        v
    Digital Twin Simulation
        |
        +-------------------+
        |                   |
        v                   v
    A* Pathfinding      Robot / AGV
                        Simulation

The backend provides persistent warehouse-related data and tasks.

The Digital Twin uses this information to maintain the simulated warehouse state and perform pathfinding and robot movement.

---

## 6. Digital Twin → Backend Updates

The Digital Twin may later send simulation state or events back to the backend, such as:

- Robot position/state
- Route completion
- Warehouse state changes
- Inventory-related simulation events
- Alerts/events

The exact API contract will be defined after backend integration requirements are finalized.

---

## 7. ML Integration

The current ML module provides demand prediction.

Current flow:

    Previous Demand
           |
           v
    Demand Prediction Model
           |
           v
    Predicted Next-Day Demand
           |
           v
    Backend
           |
           v
    Inventory / Planning
           |
           v
    Digital Twin

The current ML module should not be assumed to provide camera or sensor-based object detection.

Camera/sensor-based occupancy detection can be considered a future integration.

---

## 8. Backend vs Digital Twin Responsibility

### Backend

Responsible for:

- Persistent data
- Product records
- Shelf records
- Inventory records
- Alerts
- API access
- Database operations

### Digital Twin

Responsible for:

- Warehouse simulation
- Warehouse grid
- Simulation positions
- Robot / AGV movement
- Pathfinding
- Dynamic obstacles
- Simulation state
- Route calculation

---

## 9. Integration Principle

The Digital Twin should consume the backend's actual data contracts instead of creating incompatible duplicate schemas.

Backend-connected fields should use the existing backend naming.

Simulation-specific fields such as grid position, robot route, and dynamic obstacles should remain inside the Digital Twin unless a backend contract is explicitly defined.

Implementation will begin after this design is reviewed and approved.