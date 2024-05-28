import React from 'react'
import {
    BrowserRouter as Router,
    Route,
    Routes,
  } from "react-router-dom";

import SalePage from './pages/Sale/SalePage'
import RentPage from './pages/Rent/RentPage'
import AdminPage from './pages/Admin/AdminPage'
import HomePage from './pages/Home/HomePage';
import LoginAdmin from './pages/LoginAdmin/LoginAdmin';
import NavBar from './components/NavBar/NavBar';


export default function App() {
    return(
        <Router>
          <NavBar/>
            <Routes>
                <Route path="/" element={<HomePage/>} />
                <Route path="/rent" element={<RentPage/>} />
                <Route path="/sale" element={<SalePage/>} />
                <Route path="/admin" element={<AdminPage/>} />
                <Route path="/login" element={<LoginAdmin/>} />
            </Routes>
        </Router>
    )
}
