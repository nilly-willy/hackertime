import React from 'react';
import '../index.css'; // Ensure this path points to your index.css
import NextButton from './nextButton';

function HomePage () {
  return (
    <div className="homepage-wrapper">
      
      {/* Photo Grid */}
      <div className="photo-grid">
        <img src={require("../assets/remi1.png")} alt="Photo 1" className="photo-grid-item" />
        <img src={require("../assets/remi1.png")} alt="Photo 2" className="photo-grid-item" />
        <img src={require("../assets/remi1.png")} alt="Photo 3" className="photo-grid-item" />
        <img src={require("../assets/remi1.png")} alt="Photo 4" className="photo-grid-item" />
        <img src={require("../assets/remi1.png")} alt="Photo 5" className="photo-grid-item" />
        <img src={require("../assets/remi1.png")} alt="Photo 6" className="photo-grid-item" />
      </div>

      {/* Upload Recipe Button */}
      <div className="upload-recipe-button-container">
        <NextButton to="/input" label="upload recipe" className="upload-recipe-button"/>
      </div>

      {/* Heading: Your Health in Your Hands */}
      <div className="heading-1">
        your health in your hands
      </div>
    </div>
  );
};

export default HomePage;
