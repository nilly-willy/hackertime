import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function FinalSubmitButton() {
  // State to hold the result from the backend
  const [finalResult, setFinalResult] = useState('');
  const navigate = useNavigate();

  const handleFinalSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5001/api/submit-recipe', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: 'Submit final recipe data' }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log('Response from backend:', data);
        setFinalResult(data.result);  // Set only the result
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error sending data to backend:', error);
    }

  };

  // Helper function to format the recipe
  const formatRecipe = (recipe) => {
    if (Array.isArray(recipe)) {
      return (
        <ul>
          {recipe.map((ingredient, index) => (
            <li key={index}>{ingredient}</li>
          ))}
        </ul>
      );
    }
    return <p>{recipe}</p>;  // Handle if it's a string or other format
  };

  return (
    <div>
      <button onClick={handleFinalSubmit} style={{
        padding: '10px 20px',
        backgroundColor: '#FFA65D',
        border: 'none',
        cursor: 'pointer',
        fontSize: '16px',
        fontFamily: 'Sarpanch'
      }}>
        Show recipe
      </button>

      {/* Display only the result in a readable format */}
      {finalResult && (
        <div>
          <h3 style={{fontFamily: 'Sarpanch'}}>Here's your new recipe:</h3>
          {formatRecipe(finalResult)}
        </div>
      )}
    </div>
  );
}

export default FinalSubmitButton;
