import React from 'react';
import { Alert } from 'react-bootstrap';

function Message({ variant, children }) {
  return <Alert variant={variant}>{children}</Alert>;
}

Message.defaultProps = {
  variant: 'info', // Default style is blue
};

export default Message;
