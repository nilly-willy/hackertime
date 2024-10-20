import React, { useState } from 'react';
<<<<<<< HEAD
import Progress from './progress'; 
import NextButton from './nextButton'; 
=======
import Progress from './progress';
import NextButton from './nextButton';
>>>>>>> 104401c39648318d2154a6b1cba18a14ddcfbe19

function MainInput() {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  
  const handleClick = async () => {
    try {
      console.log('Input value before fetch:', inputValue);

<<<<<<< HEAD
=======

      fetch('http://localhost:5001/').then(res => res.text()).then(console.log)

>>>>>>> 104401c39648318d2154a6b1cba18a14ddcfbe19
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
      
      // Here you can handle the data if needed

    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };

  return (
    <div className="App">
      <Progress pvalue="0.167" />
<<<<<<< HEAD
      <input
        className="Main-text"
        type="text"
        value={inputValue}
        onChange={handleChange}
      />
      <NextButton to="/form" onClick={handleClick} label="Upload" />
=======
      <input className="Main-text"  type="text" value={inputValue} onChange={handleChange} />
      {/* <button type="submit" onClick={handleClick}>Submit</button> */}
      <NextButton to="/embed" onClick={handleClick} label="Upload"/>
>>>>>>> 104401c39648318d2154a6b1cba18a14ddcfbe19
    </div>
  );
}

export default MainInput;
