import { TextField, Button, Grid, Typography, Container } from '@mui/material';
import axios from "axios";
import {useState} from "react";

export default function LoginForm() {
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const handleSubmit = async e => {
        e.preventDefault();
        const user = {
            username: username,
            password: password
        }
        // Create the POST requuest
        const { data } = await axios.post(
            '/token/',
            user,
            {
              headers: {
                'Content-Type': 'application/json'
              },
              withCredentials: true
            }
          )

       // Initialize the access & refresh token in localstorage.      
       localStorage.clear();
       localStorage.setItem('access_token', data.access);
       localStorage.setItem('refresh_token', data.refresh);
       axios.defaults.headers.common['Authorization'] = 
                                       `Bearer ${data['access']}`;
       window.location.href = '/admin'
    }

    return (
        <Container component="main" maxWidth="xs">
          <div>
            <Typography component="h1" variant="h5">
              Sign in for admin
            </Typography>
            <form onSubmit={handleSubmit}>
              <Grid container spacing={2}>
                <Grid item xs={12}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    id="username"
                    label="Username"
                    name="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                  />
                </Grid>
                <Grid item xs={12}>
                  <TextField
                    variant="outlined"
                    required
                    fullWidth
                    name="password"
                    label="Password"
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                  />
                </Grid>
              </Grid>
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
              >
                Sign In
              </Button>
            </form>
          </div>
        </Container>
      )
}