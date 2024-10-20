import React from 'react';
import { useNavigate } from 'react-router-dom';

function NextButton({ to, onClick, label = "Next" }) {
  const navigate = useNavigate();

  const handleClick = async () => {
    // Call the onClick function passed as a prop to handle input logic
    await onClick(); // Wait for any async operation (like fetching) to complete
    navigate(to); // Then navigate to the specified path
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
