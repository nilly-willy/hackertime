import React, { useState } from 'react';
import NextButton from './nextButton';
import Progress from './progress';

function ProteinGoalInput() {
  const [proteinGoal, setProteinGoal] = useState(0);

  const handleChange = (event) => {
    setProteinGoal(event.target.value);  
  }

  // Handle form submission or button click
  const handleSubmit = async () => {
    // Convert proteinGoal to a number
    const proteinValue = Number(proteinGoal);
    console.log('Protein goal in grams:', proteinValue);  // Process the protein value

    try {
      const response = await fetch('http://localhost:5001/api/proteinGoals', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',  // Set correct content type
        },
        body: JSON.stringify({ input: proteinValue }),  // Use the protein value
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
    <div className="App">
      <Progress pvalue="0.5" />
      <label htmlFor="proteinInput">Enter your protein goal (in grams):</label>
      <input 
        id="proteinInput"
        type="number"  // Use type 'number'
        value={proteinGoal}
        onChange={handleChange}
        min="0"   // Set minimum value (optional)
        step="1"  // Increment or decrement step size
      />
      {/* <button onClick={handleSubmit}>Submit</button> */}
      <NextButton to="/scale" onClick={handleSubmit}/>
    </div>
  
  );
}

export default ProteinGoalInput;
