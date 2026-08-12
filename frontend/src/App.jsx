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

  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>AI Warehouse Automation</h1>
          <p>Smart inventory and warehouse management</p>
        </div>
      </header>

      <nav className="nav">
        {[
          "Dashboard",
          "Inventory",
          "Demand Prediction",
          "Shelf Occupancy",
          "Alerts",
        ].map((page) => (
          <button
            key={page}
            onClick={() => setActivePage(page)}
            className={activePage === page ? "active" : ""}
          >
            {page}
          </button>
        ))}
      </nav>

      <main>
        {activePage === "Dashboard" && (
          <>
            <section className="stats">
              {dashboardStats.map((stat) => (
                <div className="card" key={stat.title}>
                  <h3>{stat.title}</h3>
                  <strong>{stat.value}</strong>
                  <span>{stat.change}</span>
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
                      Warehouse monitoring and automation system is
                      operational.
                    </p>
                  </div>
                </div>
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