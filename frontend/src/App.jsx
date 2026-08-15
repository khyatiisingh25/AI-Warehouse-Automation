import { useEffect, useState } from "react";
import "./App.css";

import {
  getDashboardStats,
  getInventoryMockData,
  getDigitalTwinMockData,
} from "./api/mockApi";

import DetectionPanel from "./components/DetectionPanel";
import RobotVisualization from "./components/RobotVisualization";
import InventoryTable from "./components/InventoryTable";

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

  // ================= MOCK API STATE =================

  // Dashboard
  const [totalProducts, setTotalProducts] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  // Inventory
  const [inventory, setInventory] = useState([]);
  const [inventoryLoading, setInventoryLoading] = useState(false);
  const [inventoryError, setInventoryError] = useState("");

  // Digital Twin
  const [digitalTwin, setDigitalTwin] = useState(null);
  const [digitalTwinLoading, setDigitalTwinLoading] = useState(true);
  const [digitalTwinError, setDigitalTwinError] = useState("");

  // ================= SIDEBAR MENU =================

  const menuItems = [
    "Dashboard",
    "Inventory",
    "Products",
    "Shelves",
    "Detection",
    "Predictions",
    "Analytics",
    "Alerts",
  ];

  // ================= LOAD DASHBOARD DATA =================

  useEffect(() => {
    const loadDashboardStats = async () => {
      try {
        setLoading(true);
        setError("");

        const data = await getDashboardStats();

        setTotalProducts(data.total_products);
      } catch (err) {
        console.error("Dashboard API error:", err);
        setError("Failed to load dashboard data");
      } finally {
        setLoading(false);
      }
    };

    loadDashboardStats();
  }, []);

  // ================= LOAD INVENTORY DATA =================

  useEffect(() => {
    if (activePage !== "Inventory") {
      return;
    }

    const loadInventory = async () => {
      try {
        setInventoryLoading(true);
        setInventoryError("");

        const data = await getInventoryMockData();

        setInventory(data);
      } catch (err) {
        console.error("Inventory mock data error:", err);
        setInventoryError("Failed to load inventory");
      } finally {
        setInventoryLoading(false);
      }
    };

    loadInventory();
  }, [activePage]);

  // ================= LOAD DIGITAL TWIN DATA =================

  useEffect(() => {
    const loadDigitalTwin = async () => {
      try {
        setDigitalTwinLoading(true);
        setDigitalTwinError("");

        const data = await getDigitalTwinMockData();

        setDigitalTwin(data);
      } catch (err) {
        console.error("Digital Twin mock data error:", err);
        setDigitalTwinError("Failed to load Digital Twin data");
      } finally {
        setDigitalTwinLoading(false);
      }
    };

    loadDigitalTwin();
  }, []);

  return (
    <div className="app">
      {/* ================= SIDEBAR ================= */}

      <aside className="sidebar">
        <div className="logo">
          📦 <span>AI Warehouse</span>
        </div>

        <nav>
          {menuItems.map((item) => (
            <button
              key={item}
              className={activePage === item ? "menu active" : "menu"}
              onClick={() => setActivePage(item)}
            >
              {item}
            </button>
          ))}
        </nav>

        <div className="sidebar-bottom">
          <button className="menu">🔔 Alerts</button>
          <button className="menu">⚙️ Settings</button>
        </div>
      </aside>

      {/* ================= MAIN CONTENT ================= */}

      <main className="main-content">
        {/* ================= TOPBAR ================= */}

        <header className="topbar">
          <div>
            <h1>{activePage}</h1>
            <p>AI-powered warehouse automation system</p>
          </div>

          <div className="user">
            <div className="avatar">A</div>
            <span>Admin</span>
          </div>
        </header>

        {/* =====================================================
            DASHBOARD
        ===================================================== */}

        {activePage === "Dashboard" && (
          <>
            {/* ================= STAT CARDS ================= */}

            <section className="stats">
              {/* Total Products */}

              <div className="card">
                <h3>Total Products</h3>

                <strong>
                  {loading
                    ? "Loading..."
                    : error
                      ? "Error"
                      : totalProducts?.toLocaleString()}
                </strong>

                <span>+12% this month</span>
              </div>

              {/* Inventory Items */}

              <div className="card">
                <h3>Inventory Items</h3>

                <strong>8,542</strong>

                <span>+8% this week</span>
              </div>

              {/* Shelf Occupancy */}

              <div className="card">
                <h3>Shelf Occupancy</h3>

                <strong>76%</strong>

                <span>Healthy capacity</span>
              </div>

              {/* Active Alerts */}

              <div className="card">
                <h3>Active Alerts</h3>

                <strong>12</strong>

                <span>Needs attention</span>
              </div>
            </section>

            {/* ================= DIGITAL TWIN ================= */}

            {digitalTwinLoading ? (
              <section className="page-placeholder">
                <div className="placeholder-icon">🤖</div>

                <h2>Digital Twin</h2>

                <p>Loading warehouse simulation...</p>
              </section>
            ) : digitalTwinError ? (
              <section className="page-placeholder">
                <div className="placeholder-icon">⚠️</div>

                <h2>Digital Twin Error</h2>

                <p>{digitalTwinError}</p>
              </section>
            ) : digitalTwin ? (
              <RobotVisualization
                rows={digitalTwin.rows}
                columns={digitalTwin.columns}
                robotId={digitalTwin.robotId}
                currentPosition={digitalTwin.currentPosition}
                targetPosition={digitalTwin.targetPosition}
                route={digitalTwin.route}
                state={digitalTwin.state}
                blockedPositions={digitalTwin.blockedPositions}
                shelves={digitalTwin.shelves}
              />
            ) : null}

            {/* ================= DASHBOARD GRID ================= */}

            <section className="dashboard-grid">
              {/* Warehouse Overview */}

              <div className="panel large">
                <h2>Warehouse Overview</h2>

                <div className="warehouse-box">
                  <div className="warehouse-item">🏭</div>

                  <div>
                    <h3>AI Warehouse System</h3>

                    <p>
                      Monitor inventory, detect products and optimize
                      warehouse operations.
                    </p>
                  </div>
                </div>
              </div>

              {/* Quick Actions */}

              <div className="panel">
                <h2>Quick Actions</h2>

                <button className="action-btn">
                  🔍 Detect Products
                </button>

                <button className="action-btn">
                  📊 View Analytics
                </button>

                <button className="action-btn">
                  🤖 Generate Prediction
                </button>

                <button className="action-btn">
                  🔔 Check Alerts
                </button>
              </div>
            </section>

            {/* ================= RECENT ACTIVITY ================= */}

            <section className="panel recent">
              <h2>Recent Activity</h2>

              <div className="activity">
                <span>🟢</span>

                <div>
                  <strong>Product detected</strong>

                  <p>New product detected in Shelf A-12</p>
                </div>
              </div>

              <div className="activity">
                <span>🟡</span>

                <div>
                  <strong>Low stock alert</strong>

                  <p>Product SKU-102 is running low</p>
                </div>
              </div>

              <div className="activity">
                <span>🔵</span>

                <div>
                  <strong>Prediction generated</strong>

                  <p>Demand prediction updated successfully</p>
                </div>
              </div>
            </section>
          </>
        )}

        {/* =====================================================
            OTHER PAGES
        ===================================================== */}

        {activePage !== "Dashboard" && (
          <>
            {/* ================= DETECTION ================= */}

            {activePage === "Detection" ? (
              <DetectionPanel />
            ) : /* ================= INVENTORY ================= */

            activePage === "Inventory" ? (
              inventoryLoading ? (
                <section className="page-placeholder">
                  <div className="placeholder-icon">📦</div>

                  <h2>Inventory</h2>

                  <p>Loading inventory...</p>
                </section>
              ) : inventoryError ? (
                <section className="page-placeholder">
                  <div className="placeholder-icon">⚠️</div>

                  <h2>Inventory Error</h2>

                  <p>{inventoryError}</p>
                </section>
              ) : (
                <InventoryTable inventory={inventory} />
              )
            ) : (
              /* ================= PLACEHOLDER PAGES ================= */

              <section className="page-placeholder">
                <div className="placeholder-icon">📦</div>

                <h2>{activePage}</h2>

                <p>
                  {activePage} module will be connected with the backend API
                  here.
                </p>
              </section>
            )}
          </>
        )}
      </main>
    </div>
  );
}

export default App;