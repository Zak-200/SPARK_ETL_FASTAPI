import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000'; // URL de l'API FastAPI

export const fetchCustomers = async () => {
    try {
        const response = await axios.get(`${API_URL}/customers`);
        return response.data;
    } catch (error) {
        console.error("Error fetching customers:", error);
        throw error;
    }
};

export const fetchStats = async () => {
    try {
        const response = await axios.get(`${API_URL}/countries`);
        return response.data;
    } catch (error) {
        console.error("Error fetching stats:", error);
        throw error;
    }
};

export const addCustomer = async (customer) => {
    try {
        console.log("Données envoyées à FastAPI :", customer);  // 🔍 Vérifier ici
        const response = await axios.post(`${API_URL}/customers`, customer);
        return response.data;
    } catch (error) {
        console.error("Error adding customer:", error);
        throw error;
    }
};

export const updateCustomer = async (id, customer) => {
    try {
        const response = await axios.put(`${API_URL}/customers/${id}`, customer);
        return response.data;
    } catch (error) {
        console.error("Error updating customer:", error);
        throw error;
    }
};

export const deleteCustomer = async (id) => {
    try {
        await axios.delete(`${API_URL}/customers/${id}`);
    } catch (error) {
        console.error("Error deleting customer:", error);
        throw error;
    }
};