import React, { useState } from 'react';

function MainInput() {

  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  }

  const handleClick = async () => {

    try {
      // Send a POST request to your Python backend
      const response = await fetch('http://localhost:5000/api/process_input', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: inputValue }), // Send the input value to the backend
      });

      const data = await response.json();
      console.log('Response from backend:', data);

    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
    console.log(inputValue);
  };

  return (
    <div className="App">
      <input className="Main-text"  type="text" value={inputValue} onChange={handleChange} />
      <button type="submit" onClick={handleClick}>Submit</button>
    </div>
  );
}




export default MainInput;
