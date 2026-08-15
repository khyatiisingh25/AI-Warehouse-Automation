export const getDashboardStats = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        total_products: 1248,
      });
    }, 1000);
  });
};
export const getInventoryMockData = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve([
        {
          product_id: "PROD-001",
          product_name: "Wireless Scanner",
          sku: "SKU-WS-001",
          quantity: 120,
          minimum_stock: 20,
        },
        {
          product_id: "PROD-002",
          product_name: "Barcode Printer",
          sku: "SKU-BP-002",
          quantity: 8,
          minimum_stock: 20,
        },
        {
          product_id: "PROD-003",
          product_name: "Packing Tape",
          sku: "SKU-PT-003",
          quantity: 0,
          minimum_stock: 10,
        },
        {
          product_id: "PROD-004",
          product_name: "Storage Box",
          sku: "SKU-SB-004",
          quantity: 75,
          minimum_stock: 15,
        },
      ]);
    }, 500);
  });
};