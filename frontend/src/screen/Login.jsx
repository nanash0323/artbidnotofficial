import React, { useState } from 'react';
import { Form, Button, Container } from 'react-bootstrap';
import { useNavigate } from 'react-router-dom';
import axiosInstance from '../api/axiosInstance';

const Login = () => {
  const [formData, setFormData] = useState({
    username: '',  // Django requires "username" instead of "email" by default
    password: '',
  });
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prevData) => ({
      ...prevData,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!formData.username || !formData.password) {
      setErrorMessage('Please fill in all fields.');
      return;
    }

    try {
      const response = await axiosInstance.post('/login/', formData);

      // Save JWT token in local storage
      localStorage.setItem('authToken', response.data.access);

      console.log('Login successful!', response.data);
      navigate('/');  // Redirect to home page
    } catch (error) {
      setErrorMessage('Invalid username or password.');
    }
  };

  return (
    <Container className="my-5">
      <h2 className="text-center">Login</h2>
      <Form onSubmit={handleSubmit}>
        <Form.Group controlId="formUsername" className="mb-3">
          <Form.Label>Username</Form.Label>
          <Form.Control
            type="text"
            placeholder="Enter username"
            name="username"
            value={formData.username}
            onChange={handleChange}
          />
        </Form.Group>

        <Form.Group controlId="formPassword" className="mb-3">
          <Form.Label>Password</Form.Label>
          <Form.Control
            type="password"
            placeholder="Enter password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </Form.Group>

        {errorMessage && (
          <div className="alert alert-danger" role="alert">
            {errorMessage}
          </div>
        )}

        <Button variant="primary" type="submit" className="w-100">
          Login
        </Button>
      </Form>
    </Container>
  );
};

export default Login;
