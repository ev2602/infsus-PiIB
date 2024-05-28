import { Box, Button, CssBaseline } from "@mui/material";
import "./homePage.css"
import NavBar from "../../components/NavBar/NavBar";

const bicycles =  require("./homePageImg.jpg")

export default function HomePage() {
  return (
    <div>
        <CssBaseline />
        <Box className="box">
            <div className="mask">
                <img className="backgroundImg" src={bicycles}
                alt="backgroundImage"/>
            </div>
            <div className="content">
                <Button 
                    variant="contained" 
                    href="/rent" 
                    color="success"
                    sx={{
                        marginRight: 10
                    }}>
                    NAJAM
                </Button>
                <Button variant="contained" href="/sale" color="success">
                    PRODAJA
                </Button>
            </div>
        </Box>
        
      </div>


  );
}
