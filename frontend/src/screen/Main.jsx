import React, { useEffect, useContext } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { Row, Col, Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';
import { listProducts } from '../actions/productActions'; // Redux action
import Loader from '../components/Loader';
import Message from '../components/Message';
import { ArtContext } from '../ArtContext'; // Import the ArtContext

function Main() {
  const dispatch = useDispatch();
  const { artList = [] } = useContext(ArtContext) || {}; // Ensure artList is defined

  // Get product list from Redux state
  const productList = useSelector((state) => state.productList);
  const { loading, error, products = [] } = productList || {}; // Ensure products is defined

  useEffect(() => {
    dispatch(listProducts()); // Fetch products using Redux action
  }, [dispatch]);

  // Debugging logs
  console.log("Product List from Redux:", productList);
  console.log("Products:", products);
  console.log("Art List from Context:", artList);

  return (
    <div className="bg-black p-3">
      <h1 className="text-white text-center">Welcome to ArtBid</h1>
      <div className="d-flex justify-content-center mb-3">
        <Link to="/upload">
          <Button variant="primary">Upload Your Art</Button>
        </Link>
      </div>

      <Row xs={1} md={4} className="g-4">
        {loading ? (
          <Loader /> // Display loading spinner
        ) : error ? (
          <Message variant="danger">{error}</Message> // Show error message
        ) : (
          products.length > 0 ? (
            products.map((product) => (
              <Col key={product._id}>
                <Card className="h-100">
                  <Link to={`/product/${product._id}`}>
                    <Card.Img variant="top" src={product.image} alt={product.name} />
                  </Link>
                  <Card.Body>
                    <Link to={`/product/${product._id}`} className="text-decoration-none text-dark">
                      <Card.Title>{product.name}</Card.Title>
                    </Link>
                    <Card.Text>${product.price}</Card.Text>
                  </Card.Body>
                </Card>
              </Col>
            ))
          ) : (
            <Message variant="info">No products available.</Message>
          )
        )}

        {/* Display Uploaded Art from Context */}
        {artList.length > 0 ? (
          artList.map((art, idx) => (
            <Col key={`upload-${idx}`}>
              <Card className="h-100">
                <Card.Img variant="top" src={art.image} alt="Uploaded Art" />
                <Card.Body>
                  <Card.Title>Uploaded Art</Card.Title>
                  <Card.Text>{art.description}</Card.Text>
                </Card.Body>
              </Card>
            </Col>
          ))
        ) : (
          <Message variant="info">No uploaded art yet.</Message>
        )}
      </Row>
    </div>
  );
}

export default Main;
