import { apiClient } from "./apiClient";

export const detectProducts = async (file) => {
  const formData = new FormData();

  formData.append("file", file);

  return apiClient("/detection", {
    method: "POST",
    body: formData,
  });
};