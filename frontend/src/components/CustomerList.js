import React, { useEffect, useState } from "react";
import { fetchCustomers, deleteCustomer } from "../services/api";

const CustomerList = () => {
    const [customers, setCustomers] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadCustomers();
    }, []);

    const loadCustomers = async () => {
        setLoading(true);
        try {
            const response = await fetchCustomers();
            console.log("API Response:", response); // Log the full response
            if (Array.isArray(response)) {
                setCustomers(response);
            } else {
                console.error("Invalid API response structure:", response);
                setCustomers([]); // Set customers to an empty array
            }
        } catch (error) {
            console.error("Error fetching customers:", error);
            setCustomers([]); // Set customers to an empty array
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (id) => {
        console.log("Deleting customer with ID:", id); // Log the ID
        try {
            await deleteCustomer(id);
            loadCustomers(); // Reload the customer list after deletion
        } catch (error) {
            console.error("Error deleting customer:", error);
        }
    };

    return (
        <div>
            <h2>Liste des Clients</h2>
            {loading ? (
                <p>Chargement...</p>
            ) : (
                <table>
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>Nom</th>
                            <th>Entreprise</th>
                            <th>Pays</th>
                            <th>Email</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        {customers.length > 0 ? (
                            customers.map((customer, index) => (
                                <tr key={customer["Customer Id"] || index}>
                                    <td>{customer["Customer Id"]}</td>
                                    <td>{`${customer["First Name"]} ${customer["Last Name"]}`}</td>
                                    <td>{customer["Company"]}</td>
                                    <td>{customer["Country"]}</td>
                                    <td>{customer["Email"]}</td>
                                    <td>
                                        <button onClick={() => handleDelete(customer["Customer Id"])}>
                                            Supprimer
                                        </button>
                                    </td>
                                </tr>
                            ))
                        ) : (
                            <tr>
                                <td colSpan="6" style={{ textAlign: "center" }}>
                                    Aucun client trouvé
                                </td>
                            </tr>
                        )}
                    </tbody>
                </table>
            )}
        </div>
    );
};

export default CustomerList;