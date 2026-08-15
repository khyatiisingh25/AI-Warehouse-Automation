export const getDashboardStats = () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        total_products: 1248,
      });
    }, 1000);
  });
};