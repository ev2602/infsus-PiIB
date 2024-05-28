import * as React from 'react'
import AppBar from '@mui/material/AppBar'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import Typography from '@mui/material/Typography'
import Button from '@mui/material/Button'
import IconButton from '@mui/material/IconButton'
import ShoppingBasketIcon from '@mui/icons-material/ShoppingBasket'
import Link from '@mui/material/Link';

export default function NavBar() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar 
        position="static" 
        sx={{
            backgroundColor: "black"
        }}>
        <Toolbar>
          <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
            <Link href="/" color="inherit" underline="none">
              GetYourBike
            </Link> 
          </Typography>
          <Button 
            color="inherit" 
            sx={{ marginRight: 2}}
            href="/login">
                Admin
            </Button>
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            sx={{ mr: 2 }}
          >
             <ShoppingBasketIcon/>
          </IconButton>
        </Toolbar>
      </AppBar>
    </Box>
  );
}
