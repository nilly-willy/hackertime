import React from 'react';

function FinalSubmitButton() {
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
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };

  return (
    <button onClick={handleFinalSubmit}>
      Submit Final Recipe
    </button>
  );
}

export default FinalSubmitButton;
