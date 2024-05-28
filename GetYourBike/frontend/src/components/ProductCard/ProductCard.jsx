import { Button, Card, CardActions, CardContent, TextField, Typography } from '@mui/material';
import React, { useState } from 'react';
import axios from 'axios';

const ProductCard = ({ product, fetchBicycles }) => {
    const [isEditing, setIsEditing] = useState(false);
    const [form, setForm] = useState({
        model: product.model,
        brand: product.brand,
        category: product.category,
        pricePerDay: product.pricePerDay,
    });
    const [error, setError] = useState("");
    const [isExpanded, setIsExpanded] = useState(false)

    const handleExpand = () => {
        setIsExpanded(!isExpanded);
    }

    const handleEdit = () => {
        setIsEditing(true);
    };

    const handleCancelEdit = () => {
        setIsEditing(false);
        setForm({
            model: product.model,
            brand: product.brand,
            category: product.category,
            pricePerDay: product.pricePerDay,
        });
        setError("");
    };

    const validateForm = () => {
        const price = parseFloat(form.pricePerDay);
        if (isNaN(price) || price <= 0) {
            setError("Price per day must be a valid number greater than zero.");
            return false;
        }
        setError("");
        return true;
    };

    const handleSave = async () => {
        if (!validateForm()) {
            return;
        }

        const updatedForm = {
            ...form,
            pricePerDay: parseFloat(form.pricePerDay),
        };

        try {
            await axios.put(`/api/rentBicycles/${product.id}/`, updatedForm); // Use POST instead of PUT
            setIsEditing(false);
            fetchBicycles();
        } catch (error) {
            console.error('Error updating the bicycle:', error.response.data);
            setError("Failed to update the bicycle. Please try again.");
        }
    };

    const handleDelete = async () => {
        try {
            await axios.delete(`/api/rentBicycles/${product.id}/`);
            fetchBicycles();
        } catch (error) {
            console.error('Error deleting the bicycle:', error.response.data);
            setError("Failed to delete the bicycle. Please try again.");
        }
    };

    return (
        <Card sx={{ height: "auto", width: "100%", marginBottom: "1px", cursor: 'pointer'}}>
            <CardContent onClick={handleExpand}>
                <Typography variant="h6">
                    {product.model}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Brand: {product.brand}
                </Typography>
                {isExpanded &&
                <>
                <Typography variant="body2" color="text.secondary">
                    Category: {product.category}
                </Typography>
                <Typography variant="body2" color="text.secondary">
                    Reserved Dates: {product.reservedDates.join(", ")}
                </Typography>
                {isEditing ? (
                    <>
                        <TextField
                            label="Price Per Day"
                            value={form.pricePerDay}
                            onChange={(e) => setForm({ ...form, pricePerDay: e.target.value })}
                            fullWidth
                            margin="dense"
                            type="number" // Ensure this field is a number input
                        />
                        {error && (
                            <Typography color="error" variant="body2">
                                {error}
                            </Typography>
                        )}
                    </>
                ) : (
                    <>
                        <Typography variant="body2" color="text.secondary">
                            Price per Day: {product.pricePerDay}€
                        </Typography>
                    </>
                )}
                </> }
            </CardContent>
            <CardActions>
                {isExpanded && ( isEditing ? (
                    <>
                        <Button size="small" onClick={handleSave}>Save</Button>
                        <Button size="small" onClick={handleCancelEdit}>Cancel</Button>
                    </>
                ) : (
                    <>
                        <Button size="small" onClick={handleEdit}>Edit</Button>
                        <Button size="small" onClick={handleDelete}>Delete</Button>
                    </>
                ))}
            </CardActions>
        </Card>
    );
};

export default ProductCard;
