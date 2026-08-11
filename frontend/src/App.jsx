import { useState } from "react";
import "./App.css";

function App() {
  const [activePage, setActivePage] = useState("Dashboard");

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

  return (
    <div className="app">
      {/* Sidebar */}
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

      {/* Main Content */}
      <main className="main-content">
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

        {/* Dashboard */}
        {activePage === "Dashboard" && (
          <>
            <section className="stats">
              <div className="card">
                <h3>Total Products</h3>
                <strong>1,248</strong>
                <span>+12% this month</span>
              </div>

              <div className="card">
                <h3>Inventory Items</h3>
                <strong>8,542</strong>
                <span>+8% this week</span>
              </div>

              <div className="card">
                <h3>Shelf Occupancy</h3>
                <strong>76%</strong>
                <span>Healthy capacity</span>
              </div>

              <div className="card">
                <h3>Active Alerts</h3>
                <strong>12</strong>
                <span>Needs attention</span>
              </div>
            </section>

            <section className="dashboard-grid">
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

        {/* Other Pages */}
        {activePage !== "Dashboard" && (
          <section className="page-placeholder">
            <div className="placeholder-icon">📦</div>
            <h2>{activePage}</h2>
            <p>
              {activePage} module is ready for integration here
              here.
            </p>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;