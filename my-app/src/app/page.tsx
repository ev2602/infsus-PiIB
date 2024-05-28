import { Box, Button, CssBaseline } from "@mui/material";
import "./homePage.css"

export default function Home() {
  return (
    <div>
        <CssBaseline />
        <Box className="box">
            <div className="mask">
                <img className="backgroundImg" src="/homePageImg.jpg"
                alt="backgroundImage"/>
            </div>
            <div className="content">
                <Button variant="contained" href="/rent" color="success">
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
