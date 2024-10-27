import logo from './logo.svg';
import './App.css';
import Box from '@mui/material/Box';
import Container from '@mui/material/Container';
import ResponsiveAppBar from './components/AppBar';
import Feed from './pages/Feed/Feed-card';

function App() {
  return (
      <Container maxWidth="lg">
          <ResponsiveAppBar sx={{marginBottom: 10 }} />
          <Feed />

      </Container>
  );
}

export default App;
