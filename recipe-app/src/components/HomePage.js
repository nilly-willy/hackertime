import React from 'react';
import '../index.css'; // Ensure this path points to your index.css
import NextButton from './nextButton';

function HomePage () {
  return (
    <div className="homepage-wrapper">
      {/* Photo Grid */}
      <div className="photo-grid">
        <img src={require("../assets/remi1.png")} alt="Photo 0" className="photo-grid-item" />
        <img src={require("../assets/4.jpg")} alt="Photo 1" className="photo-grid-item" />
        <img src={require("../assets/1.jpg")} alt="Photo 2" className="photo-grid-item" />
        <img src={require("../assets/3.jpg")} alt="Photo 4" className="photo-grid-item" />
      </div>

      {/* New Heading: REMI: AI Chef */}
      <h1 className="ai-chef-heading">REMI: AI Chef</h1>

      {/* Upload Recipe Button */}
      <div className="upload-recipe-button-container">
        <NextButton to="/input" label="Upload Recipe" className="upload-recipe-button"/>
      </div>

      {/* Heading: Your Health in Your Hands */}
      <div className="heading-1">
        your health in your hands
      </div>
    </div>
  );
};

export default HomePage;
