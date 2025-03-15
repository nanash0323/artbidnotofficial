import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Main from './screen/Main';
import Login from './screen/Login';
import SignUp from './screen/SignUp';
import Profile from './components/Profile/Profile';
import UploadScreen from './screen/UploadScreen'; // Import UploadScreen
import { ArtProvider } from './ArtContext'; // Import ArtProvider
import 'bootstrap/dist/css/bootstrap.min.css';

function App() {
  return (
    <ArtProvider> {/* Wrap the entire application with ArtProvider */}
      <Router>
        <div className="app-container">
          <Header />
          <Routes>
            <Route path="/" element={<Main />} /> {/* Main gallery screen */}
            <Route path="/login" element={<Login />} />
            <Route path="/signup" element={<SignUp />} />
            <Route path="/profile" element={<Profile />} /> {/* Profile page */}
            <Route path="/upload" element={<UploadScreen />} /> {/* Upload Art Page */}
          </Routes>
          <Footer />
        </div>
      </Router>
    </ArtProvider>
  );
}

export default App;
