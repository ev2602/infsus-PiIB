import axios from "axios";
import { useEffect, useState } from 'react';
import { Container, Typography, Grid, Button, TextField, Dialog, DialogActions, DialogContent, DialogTitle, FormControl, InputLabel, Select, MenuItem } from '@mui/material';
import ProductCard from "../../components/ProductCard/ProductCard";

export default function AdminPage() {
    const [bicycles, setBicycles] = useState([]);
    const [open, setOpen] = useState(false);
    const [newProductRent, setNewProductRent] = useState({
        brand: '',
        model: '',
        category: '',
        reservedDates: [],
        pricePerDay: ''
    });
    const [categories, setCategories] = useState([]);

    const fetchBicycles = async () => {
        const response = await axios.get('/api/rentBicycles/');
        setBicycles(response.data);
    };

    const fetchCategories = async () => {
        const response = await axios.get('/api/category/');
        setCategories(response.data);
    };

    useEffect(() => {
        fetchBicycles();
        fetchCategories();
    }, []);

    const handleOpen = () => {
        setOpen(true);
    };

    const handleClose = () => {
        setOpen(false);
        setNewProductRent({
            brand: '',
            model: '',
            category: '',
            reservedDates: [],
            pricePerDay: ''
        });
    };

    const handleSave = async () => {
        await axios.post('/api/rentBicycles/', newProductRent);
        fetchBicycles();
        handleClose();
    };

    return (
        <Container maxWidth="lg">
            <Typography variant="h4" align="center" gutterBottom>
                Admin Page
            </Typography>
            <Typography variant="h5" align="center" gutterBottom>
                Products Available for Rent
            </Typography>
            <Button variant="contained" color="primary" onClick={handleOpen}>
                Add New Bicycle
            </Button>
            <Dialog open={open} onClose={handleClose}>
                <DialogTitle>Add New Product</DialogTitle>
                <DialogContent>
                    <TextField
                        label="Brand"
                        value={newProductRent.brand}
                        onChange={(e) => setNewProductRent({ ...newProductRent, brand: e.target.value })}
                        fullWidth
                        margin="dense"
                        inputProps={{ "data-testid": "brand-input" }}
                    />
                    <TextField
                        label="Model"
                        value={newProductRent.model}
                        onChange={(e) => setNewProductRent({ ...newProductRent, model: e.target.value })}
                        fullWidth
                        margin="dense"
                        inputProps={{ "data-testid": "model-input" }}
                    />
                    <FormControl fullWidth margin="dense">
                        <InputLabel id="category-label" inputProps={{ "data-testid": "category-select" }}>Category</InputLabel>
                        <Select
                            labelId="category-label"
                            value={newProductRent.category}
                            onChange={(e) => setNewProductRent({ ...newProductRent, category: e.target.value })}
                        >
                            {categories.map(category => (
                                <MenuItem key={category.id} value={category.id}>{category.name}</MenuItem>
                            ))}
                        </Select>
                    </FormControl>
                    <TextField
                        label="Reserved Dates (comma-separated)"
                        value={newProductRent.reservedDates}
                        onChange={(e) => setNewProductRent({ ...newProductRent, reservedDates: e.target.value.split(',') })}
                        fullWidth
                        margin="dense"
                        inputProps={{ "data-testid": "reserved-dates-input" }}
                    />
                    <TextField
                        label="Price Per Day"
                        value={newProductRent.pricePerDay}
                        onChange={(e) => setNewProductRent({ ...newProductRent, pricePerDay: e.target.value })}
                        fullWidth
                        margin="dense"
                        inputProps={{ "data-testid": "price-per-day-input" }}
                    />
                </DialogContent>
                <DialogActions>
                    <Button onClick={handleClose} color="secondary">
                        Cancel
                    </Button>
                    <Button onClick={handleSave} color="primary">
                        Save
                    </Button>
                </DialogActions>
            </Dialog>
            <Grid container spacing={3}>
                {bicycles.map(bicycle => (
                    <Grid item xs={12} sm={6} md={4} key={bicycle.id}>
                        <ProductCard product={bicycle} fetchBicycles={fetchBicycles} />
                    </Grid>
                ))}
            </Grid>
        </Container>
    );
}
