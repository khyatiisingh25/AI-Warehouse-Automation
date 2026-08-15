const getStatus = (quantity, minimumStock) => {
  if (quantity === 0) {
    return {
      label: "Out of Stock",
      className: "out-of-stock",
    };
  }

  if (quantity <= minimumStock) {
    return {
      label: "Low Stock",
      className: "low-stock",
    };
  }

  return {
    label: "Healthy",
    className: "healthy",
  };
};

function InventoryStatusBadge({ quantity, minimumStock }) {
  const status = getStatus(quantity, minimumStock);

  return (
    <span className={`inventory-status ${status.className}`}>
      {status.label}
    </span>
  );
}

export default InventoryStatusBadge;