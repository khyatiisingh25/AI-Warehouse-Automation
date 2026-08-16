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
export const getDigitalTwinMockData = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        rows: 8,
        columns: 10,
        robotId: "AGV-01",

        currentPosition: {
          row: 2,
          column: 3,
        },

        targetPosition: {
          row: 5,
          column: 7,
        },

        route: [
          { row: 2, column: 3 },
          { row: 2, column: 4 },
          { row: 2, column: 5 },
          { row: 3, column: 5 },
          { row: 4, column: 5 },
          { row: 5, column: 5 },
          { row: 5, column: 6 },
          { row: 5, column: 7 },
        ],

        state: "MOVING",

        blockedPositions: [
          { row: 1, column: 2 },
          { row: 4, column: 4 },
        ],

        shelves: [
          { row: 1, column: 5, shelfId: "S-01" },
          { row: 3, column: 2, shelfId: "S-02" },
          { row: 6, column: 8, shelfId: "S-03" },
        ],
      });
    }, 500);
  });
};