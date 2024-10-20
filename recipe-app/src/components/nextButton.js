import React from 'react';
import { useNavigate } from 'react-router-dom';

function NextButton({ to, label = "Next", onClick }) {
  const navigate = useNavigate();

  const handleClick = async (e) => {
    if (onClick) {
      await onClick(e); // Execute the onClick passed as a prop
    }
    navigate(to); // Navigate to the specified path
  };

  return (
    <button 
      onClick={handleClick}
      style={{
        padding: '10px 20px',
        backgroundColor: '#FFA65D',
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
