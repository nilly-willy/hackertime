import React, { useState } from 'react';
import Progress from './progress';
import NextButton from './nextButton';

function MainInput() {
  const [inputValue, setInputValue] = useState('');

  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  
  const handleClick = async () => {
    console.log("entered handle click")
    try {
      console.log('Input value before fetch:', inputValue);


      fetch('http://localhost:5000/').then(res => res.text()).then(console.log)

      const response = await fetch('http://localhost:5000/api/process_input', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: inputValue }),
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      // const data = await response.json();
      // console.log('Response from backend:', data);
      
      // Here you can handle the data if needed

    } catch (error) {
      console.error('Error sending data to backend:', error);
    }
  };

  return (
    <div className="App">
      <Progress pvalue="0.167" />
      <input className="Main-text"  type="text" value={inputValue} onChange={handleChange} />
      {/* <button type="submit" onClick={handleClick}>Submit</button> */}
      <NextButton to="/embed" type="submit" onClick={handleClick} label="Upload"/>
    </div>
  );
}

export default MainInput;
