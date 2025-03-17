import axiosInstance from "./axiosInstance";

// ✅ Register API
export const registerUser = async (userData) => {
  try {
    const response = await axiosInstance.post("/register/", userData);
    return response.data;
  } catch (error) {
    return error.response?.data || { error: "Registration failed" };
  }
};

// ✅ Login API
export const loginUser = async (credentials) => {
  try {
    const response = await axiosInstance.post("/login/", credentials);
    localStorage.setItem("authToken", response.data.access);
    localStorage.setItem("refreshToken", response.data.refresh);
    return response.data;
  } catch (error) {
    return error.response?.data || { error: "Login failed" };
  }
};

// ✅ Logout API
export const logoutUser = async () => {
  try {
    const refreshToken = localStorage.getItem("refreshToken");
    await axiosInstance.post("/logout/", { refresh_token: refreshToken });
    localStorage.removeItem("authToken");
    localStorage.removeItem("refreshToken");
  } catch (error) {
    console.error("Logout failed:", error);
  }
};
