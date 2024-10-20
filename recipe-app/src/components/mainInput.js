import React, { useState } from 'react';
import Progress from './progress';
import NextButton from './nextButton';

function MainInput() {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleClick = async () => {
    console.log("entered handle click");
    try {
      console.log('Input value before fetch:', inputValue);

      fetch('http://localhost:5001/').then(res => res.text()).then(console.log);

      const response = await fetch('http://localhost:5001/api/process_input', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: inputValue }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log('Response from backend:', data);
      
      // Handle the data if needed

    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };

  return (
    <div className="App" style={{ display: 'flex', flexDirection: 'column', gap: '10px', margin: '50px', fontFamily: 'Sarpanch, sans-serif' }}>
      <Progress pvalue="0.167" />
      <h2 style={{ margin: '0', fontFamily: 'Sarpanch, sans-serif', textAlign: 'center'}}>Upload Recipe Here</h2>
      <textarea
        className="Main-text"
        value={inputValue}
        onChange={handleChange}
        style={{
          padding: '12px 20px',
          height: '100px', // Adjust height as needed
          resize: 'vertical', // Allow vertical resizing
          overflow: 'auto', // Add scroll if necessary
          fontFamily: 'Sarpanch, sans-serif', // Apply the font here as well
          
        }}
      />
      <NextButton
        to="/form"
        type="submit"
        onClick={handleClick}
        label="Upload"
        style={{
          padding: '10px 20px',
          border: 'none',
          cursor: 'pointer',
          width: 'fit-content',
          fontFamily: 'Sarpanch, sans-serif' 
          
        }}
      />
    </div>
  );
}

export default MainInput;
