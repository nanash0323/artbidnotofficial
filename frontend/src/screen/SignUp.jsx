import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Form, Button, Container } from "react-bootstrap";
import axios from "axios";

const SignUp = () => {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [errorMessage, setErrorMessage] = useState("");
  const navigate = useNavigate();

  // Handle form input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (formData.password !== formData.confirmPassword) {
      setErrorMessage("Passwords do not match.");
      return;
    }
    if (!formData.username || !formData.email || !formData.password) {
      setErrorMessage("All fields are required.");
      return;
    }

    try {
      const response = await axios.post("http://127.0.0.1:8000/api/register/", {
        username: formData.username,
        email: formData.email,
        password: formData.password,
      });

      console.log("Signup successful:", response.data);

      // Store token (optional)
      localStorage.setItem("access", response.data.access);
      localStorage.setItem("refresh", response.data.refresh);

      // Redirect to login
      navigate("/login");
    } catch (error) {
      console.error("Signup error:", error);
      setErrorMessage("Signup failed. Please try again.");
    }
  };

  return (
    <Container className="my-5">
      <h2 className="text-center">Sign Up</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formUsername" className="mb-3">
          <Form.Label>Username</Form.Label>
          <Form.Control type="text" name="username" value={formData.username} onChange={handleChange} />
        </Form.Group>

        <Form.Group controlId="formEmail" className="mb-3">
          <Form.Label>Email</Form.Label>
          <Form.Control type="email" name="email" value={formData.email} onChange={handleChange} />
        </Form.Group>

        <Form.Group controlId="formPassword" className="mb-3">
          <Form.Label>Password</Form.Label>
          <Form.Control type="password" name="password" value={formData.password} onChange={handleChange} />
        </Form.Group>

        <Form.Group controlId="formConfirmPassword" className="mb-3">
          <Form.Label>Confirm Password</Form.Label>
          <Form.Control type="password" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />
        </Form.Group>

        {errorMessage && <div className="alert alert-danger">{errorMessage}</div>}

        <Button type="submit" className="w-100">Sign Up</Button>
      </Form>

      <div className="text-center mt-3">
        <p>
          Already have an account? <a href="/login">Login here</a>
        </p>
      </div>
    </Container>
  );
};

export default SignUp;
