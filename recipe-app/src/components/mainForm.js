import React, { useState } from 'react';
import NextButton from './nextButton';
import Progress from './progress';


function MainForm() {  
  // Health Conditions
  const healthOptions = ['Diabetes', 'High Blood Pressure', 'Kidney Disease', 'Stroke', 'Heart Disease', 'Pregnancy', 'Celiacs Disease'];
  const [health, setHealth] = useState([]);

  //Dietary Restrictions
  const dietOptions = ["Dairy Free", "Gluten Free", "Allergen: Wheat", "Allergen: Nuts", "Allergen: Shellfish", "Allergen: Soy", "Allergen: Eggs"];
  const [diet, setDiet] = useState([]);

  // Health Handler
  const handleHealth = (option) => {
    setHealth((prevhealth) => {
      if (prevhealth.includes(option)) {
        // Remove the option if it's already in health
        return prevhealth.filter((item) => item !== option);
      } else {
        // Add the option if it's not in health
        return [...prevhealth, option];
      }
    });
  };

  // Diet Handler
  const handleDiet = (option) => {
    setDiet((prevDiet) => {
      if (prevDiet.includes(option)) {
        // Remove the option if it's already in diet
        return prevDiet.filter((item) => item !== option);
      } else {
        // Add the option if it's not in diet 
        return [...prevDiet, option];
      }
    });
  };

  const sendDataToBackend = async() => {
    console.log(health);
    try {
        console.log("fetching right now...")
        await fetch('http://localhost:5001/api/submit-selections', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify( [health, diet] ), // Sending the health array
      });
      // const data = await response.json();
      // console.log(data);
    } catch (error) {
      console.log("Caught error: ", error)
    }
  }

  return (
    <div>
      <Progress pvalue="0.333" />
      <h3>Health Conditions</h3>
      <div style={{ display: 'flex', gap: '10px' }}>
        {healthOptions.map((option) => (
          <button
            key={option}
            onClick={() => handleHealth(option)}
            style={{
              padding: '10px 20px',
              border: 'none',
              cursor: 'pointer',
            }}
          >
            {option}
          </button>
        ))}
      </div>

      <h3> Dietary Restrictions </h3>
      <div style={{ display: 'flex', gap: '10px' }}>
        {dietOptions.map((option) => (
          <button
            key={option}
            onClick={() => handleDiet(option)}
            style={{
              padding: '10px 20px',
              border: 'none',
              cursor: 'pointer',
            }}
          >
            {option}
          </button>
        ))}
      </div>

      {/* <button 
        onClick={sendDataToBackend} 
        style={{ 
          marginTop: '20px',
          padding: '10px 20px',
          backgroundColor:'lightgray',
          border: 'none',
          cursor: 'pointer',
        }}>
        Submit
      </button> */}
      
      <NextButton to="/protein" onClick={sendDataToBackend} />
    </div>

  );
}

export default MainForm;