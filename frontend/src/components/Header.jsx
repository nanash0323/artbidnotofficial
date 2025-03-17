import React, { useEffect, useState, useCallback } from "react";
import { NavLink, useNavigate } from "react-router-dom";
import { logoutUser } from "../api/authApi";
import Button from "react-bootstrap/Button";
import Container from "react-bootstrap/Container";
import Form from "react-bootstrap/Form";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import NavDropdown from "react-bootstrap/NavDropdown";

function Header() {
  const navigate = useNavigate();
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  // Function to check if the token is expired
  function isTokenExpired(token) {
    try {
      const decoded = JSON.parse(atob(token.split(".")[1])); // Decode JWT payload
      return decoded.exp * 1000 < Date.now(); // Check if token is expired
    } catch (e) {
      return true; // Treat invalid tokens as expired
    }
  }

  // ✅ Memoized function to check authentication status
  const checkAuth = useCallback(() => {
    const token = localStorage.getItem("authToken");
    setIsAuthenticated(token && !isTokenExpired(token));
  }, []);

  useEffect(() => {
    checkAuth(); // Run on mount

    // ✅ Listen for storage changes to detect login/logout
    const handleStorageChange = () => checkAuth();
    window.addEventListener("storage", handleStorageChange);
    
    return () => {
      window.removeEventListener("storage", handleStorageChange);
    };
  }, [checkAuth]);

  const handleLogout = async () => {
    await logoutUser();
    setIsAuthenticated(false);
    navigate("/login");
  };

  return (
    <Navbar expand="lg" className="bg-black">
      <Container fluid>
        <Navbar.Brand as={NavLink} to="/" style={{ color: "white" }}>
          ArtBid
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav className="me-auto my-2 my-lg-0" navbarScroll>
            <Nav.Link as={NavLink} to="/" style={{ color: "white" }}>
              Home
            </Nav.Link>
            <Nav.Link as={NavLink} to="/profile" style={{ color: "white" }}>
              Profile
            </Nav.Link>
            <NavDropdown title={<span style={{ color: "white" }}>Inventory</span>} id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action4">Another action</NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">Something else here</NavDropdown.Item>
            </NavDropdown>

            {/* Conditional Rendering for Authentication */}
            {!isAuthenticated ? (
              <>
                <Nav.Link as={NavLink} to="/signup" style={{ color: "white" }}>
                  Sign Up
                </Nav.Link>
                <Nav.Link as={NavLink} to="/login" style={{ color: "white" }}>
                  Login
                </Nav.Link>
              </>
            ) : (
              <Nav.Link href="#" style={{ color: "white" }} onClick={handleLogout}>
                Logout
              </Nav.Link>
            )}
          </Nav>

          {/* Search Bar */}
          <Form className="d-flex">
            <Form.Control type="search" placeholder="Search" className="me-2" aria-label="Search" />
            <Button variant="outline-light">Search</Button>
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Header;
