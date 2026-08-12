import { useState } from "react";
import "./App.css";
const dashboardStats = [
  {
    title: "Total Products",
    value: "1,248",
    change: "+12% this month",
  },
  {
    title: "Inventory Items",
    value: "8,542",
    change: "+8% this week",
  },
  {
    title: "Shelf Occupancy",
    value: "76%",
    change: "Healthy capacity",
  },
  {
    title: "Active Alerts",
    value: "12",
    change: "Needs attention",
  },
];

const recentActivities = [
  {
    icon: "🟢",
    title: "Product detected",
    description: "New product detected in Shelf A-12",
  },
  {
    icon: "🟡",
    title: "Low stock alert",
    description: "Product SKU-102 is running low",
  },
  {
    icon: "🔵",
    title: "Prediction generated",
    description: "Demand prediction updated successfully",
  },
];

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
              {dashboardStats.map((stat) => (
                <div className="card" key={stat.title}>
                  <h3>{stat.title}</h3>
                  <strong>{stat.value}</strong>
                  <span>{stat.info}</span>
                </div>
              ))}
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

              {recentActivities.map((activity) => (
                <div className="activity" key={activity.title}>
                  <span>{activity.icon}</span>
                  <div>
                    <strong>{activity.title}</strong>
                    <p>{activity.description}</p>
                  </div>
                </div>
              ))}
            </section>
          </>
        )}

        {/* Other Pages */}
        {activePage !== "Dashboard" && (
          <section className="page-placeholder">
            <div className="placeholder-icon">📦</div>

            <h2>{activePage}</h2>

            <p>
              {activePage} module is ready for integration here.
            </p>
          </section>
        )}
      </main>
    </div>
  );
}

export default App;