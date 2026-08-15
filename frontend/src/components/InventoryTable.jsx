import InventoryStatusBadge from "./InventoryStatusBadge";

function InventoryTable({ inventory = [] }) {
  if (inventory.length === 0) {
    return (
      <section className="inventory-section">
        <div className="inventory-empty">
          <div className="inventory-empty__icon">📦</div>
          <h3>No Inventory Found</h3>
          <p>There are currently no inventory items to display.</p>
        </div>
      </section>
    );
  }

  return (
    <section className="inventory-section">
      <div className="inventory-section__header">
        <div>
          <h2>Inventory</h2>
          <p>Current warehouse stock overview</p>
        </div>

        <span className="inventory-count">
          {inventory.length} items
        </span>
      </div>

      <div className="inventory-table-wrapper">
        <table className="inventory-table">
          <thead>
            <tr>
              <th>Product</th>
              <th>SKU / ID</th>
              <th>Stock</th>
              <th>Reorder Level</th>
              <th>Status</th>
            </tr>
          </thead>

          <tbody>
            {inventory.map((item) => (
              <tr key={item.product_id}>
                <td>
                  <div className="inventory-product">
                    <strong>{item.product_name}</strong>
                    <span>{item.product_id}</span>
                  </div>
                </td>

                <td>{item.sku}</td>

                <td>
                  <strong>{item.quantity}</strong>
                </td>

                <td>{item.minimum_stock}</td>

                <td>
                  <InventoryStatusBadge
                    quantity={item.quantity}
                    minimumStock={item.minimum_stock}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </section>
  );
}

export default InventoryTable;