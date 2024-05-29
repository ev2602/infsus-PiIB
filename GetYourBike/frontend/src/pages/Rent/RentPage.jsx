import React, { useState, useEffect } from 'react';
import axios from 'axios';
import NavBar from '../../components/NavBar/NavBar';
import { Typography, TextField, MenuItem } from '@mui/material';
import BicycleCard from '../../components/BicycleCard/BicycleCard';
import './RentPage.css';
import bicycle from './bicycle.jpg';

export default function RentPage() {
  const [bicycles, setBicycles] = useState([]);
  const [searchTerm, setSearchTerm] = useState('');
  const [priceRange, setPriceRange] = useState([0, 100000]);
  const [categoryFilter, setCategoryFilter] = useState('');
  const [brandFilter, setBrandFilter] = useState('');
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetchBicycles();
    fetchCategories();
  }, []);

  const fetchBicycles = async () => {
    const response = await axios.get('/api/rentBicycles/');
    setBicycles(response.data);
  };

  const fetchCategories = async () => {
    const response = await axios.get('api/category/');
    setCategories(response.data);
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const handlePriceRangeChange = (event) => {
    setPriceRange(event.target.value);
  };

  const handleCategoryFilterChange = (event) => {
    setCategoryFilter(event.target.value);
  };

  const handleBrandFilterChange = (event) => {
    setBrandFilter(event.target.value);
  };

  const getCategoryNameById = (categoryId) => {
    const category = categories.find((category) => category.id === categoryId);
    return category ? category.name : '';
  };

  const filteredBicycles = bicycles.filter((bicycle) => {
    const { model, brand, category, pricePerDay } = bicycle;
    const searchLowerCase = searchTerm.toLowerCase();
    console.log("Price", priceRange[0])

    const priceInRange =
    (priceRange[0] <= pricePerDay && priceRange[1] >= pricePerDay)
    
    const searchedBicycles = ( model.toLowerCase().includes(searchLowerCase) ||
    brand.toLowerCase().includes(searchLowerCase) ||
    getCategoryNameById(category).toLowerCase().includes(searchLowerCase))
    return (
      searchedBicycles &&
      (brand.toLowerCase().includes(brandFilter.toLowerCase()) || !brandFilter) &&
      (getCategoryNameById(category).toLowerCase().includes(categoryFilter.toLowerCase()) || !categoryFilter) 
      && priceInRange
    );
  });

  return (
    <div>
      <Typography
        variant="h2"
        sx={{
          textAlign: 'center',
          padding: '10px',
          fontFamily: 'Work Sans, sans-serif',
        }}
      >
        Bicikli za najam
      </Typography>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <TextField
          label="Search"
          variant="outlined"
          value={searchTerm}
          onChange={handleSearch}
          sx={{ marginBottom: '20px', marginRight: '20px' }}
        />
        <TextField
          select
          label="Price Range"
          variant="outlined"
          value={priceRange}
          onChange={handlePriceRangeChange}
          sx={{ marginBottom: '20px', marginRight: '20px', width: "100px" }}
        >
          <MenuItem value={[0,100000]}>All</MenuItem>
          <MenuItem value={[0,10]}>0-10€</MenuItem>
          <MenuItem value={[10,15]}>10-15€</MenuItem>
          <MenuItem value={[15,20]}>15-20€</MenuItem>
          <MenuItem value={[20,10000]}>20€+</MenuItem>
        </TextField>
        <TextField
          select
          label="Category"
          variant="outlined"
          value={categoryFilter}
          onChange={handleCategoryFilterChange}
          sx={{ marginBottom: '20px', marginRight: '20px', width: "100px" }}
        >
          <MenuItem value="">All</MenuItem>
          {categories.map((category) => (
            <MenuItem key={category.id} value={category.name}>{category.name}</MenuItem>
          ))}
        </TextField>
        <TextField
          label="Brand"
          variant="outlined"
          value={brandFilter}
          onChange={handleBrandFilterChange}
          sx={{ marginBottom: '20px', marginRight: '20px' }}
        />
      </div>
      <div className="card-container">
        {filteredBicycles.map((bicycle) => (
          <BicycleCard bicycle={bicycle} category={getCategoryNameById(bicycle.category)} key={bicycle.id} />
        ))}
      </div>
    </div>
  );
}
