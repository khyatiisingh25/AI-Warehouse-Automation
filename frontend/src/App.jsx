import { useEffect, useState } from "react";
import "./App.css";
import { getDashboardStats } from "./api/mockApi";

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

  // Mock API state
  const [totalProducts, setTotalProducts] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

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

  // Load dashboard data from mock API
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

        {/* ================= DASHBOARD ================= */}
        {activePage === "Dashboard" && (
          <>
            {/* ================= STAT CARDS ================= */}
            <section className="stats">
              {/* Total Products - Mock API */}
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

        {/* ================= OTHER PAGES ================= */}
        {activePage !== "Dashboard" && (
          <section className="page-placeholder">
            <div className="placeholder-icon">📦</div>

            <h2>{activePage}</h2>

            <p>
              {activePage} module will be connected with the backend API
              here.
            </p>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;