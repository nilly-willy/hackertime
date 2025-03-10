import React, { useState } from 'react';
import NextButton from './nextButton';
import Progress from './progress';

function ScalingInput() {
  const [inputValue, setInputValue] = useState(0);

  const handleChange = (event) => {
    setInputValue(event.target.value);  
  }

  // Handle form submission or button click
  const handleSubmit = async () => {
    // Convert inputValue to a number
    const numberValue = Number(inputValue);
    console.log('Selected number:', numberValue);  // Process the number value

    try {
      const response = await fetch('http://localhost:5001/api/scaling', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',  // Set correct content type
        },
        body: JSON.stringify({ input: numberValue }),  // Use the number value
        // credentials: 'include',  // Include this if needed
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
      <Progress pvalue="0.667" />
      <label htmlFor="numberInput">Scale your recipe:</label>
      <input 
        id="numberInput"
        type="number"  // Use type 'number'
        value={inputValue}
        onChange={handleChange}
        min="0"   // Set minimum value (optional)
        max="100" // Set maximum value (optional)
        step="1"  // Increment or decrement step size
      />
      {/* <button onClick={handleSubmit}>Submit</button> */}
      <div style={{margin: '25px 15px 25px 0px'}}>
      <NextButton to="/load" onClick={handleSubmit} label="get my new recipe!"/>
      </div>
    </div>
  );
}

export default ScalingInput;
