import React, { useEffect, useState } from "react";
import { fetchStats } from "../services/api";
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid, Legend } from "recharts";

const Dashboard = () => {
    const [stats, setStats] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        loadStats();
    }, []);

    const loadStats = async () => {
        setLoading(true);
        setError(null);
        try {
            const response = await fetchStats();
            console.log("API Response:", response); // Log pour voir les données

            if (response && Array.isArray(response.countries)) {
                setStats(response.countries);
            } else {
                throw new Error("Format de réponse invalide");
            }
        } catch (err) {
            console.error("Erreur lors du chargement des statistiques:", err);
            setError("Erreur lors du chargement des statistiques");
            setStats([]); // Évite les crashs si le graphique attend des données
        } finally {
            setLoading(false);
        }
    };

    return (
        <div style={{ width: "100%", maxWidth: "800px", margin: "20px auto", textAlign: "center" }}>
            <h2>📊 Statistiques des Clients par Pays</h2>

            {loading ? (
                <p>Chargement des données...</p>
            ) : error ? (
                <p style={{ color: "red", fontWeight: "bold" }}>{error}</p>
            ) : stats.length === 0 ? (
                <p>Aucune donnée disponible</p>
            ) : (
                <ResponsiveContainer width="100%" height={400}>
                    <BarChart data={stats} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="_id" tick={{ fontSize: 14 }} />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="count" fill="#ff6b6b" barSize={50} />
                    </BarChart>
                </ResponsiveContainer>
            )}
        </div>
    );
};

export default Dashboard;
