import React from 'react';
import { useNavigate } from 'react-router-dom';

function NextButton({ to, label = "Next" }) {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(to); // Navigate to the specified path
  };

  return (
    <button 
      onClick={handleClick}
      style={{
        padding: '10px 20px',
        backgroundColor: 'lightblue',
        border: 'none',
        cursor: 'pointer',
        fontSize: '16px'
      }}
    >
      {label}
    </button>
  );
}

export default NextButton;
