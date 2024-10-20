import React from 'react';
import '../index.css'; // Ensure this path points to your index.css

const HomePage = () => {
  return (
    <div className="homepage-wrapper" style={{ width: '100%', height: '100%', position: 'relative', background: 'white' }}>
      
      {/* Logo */}
      <div className="logo-container" style={{ position: 'absolute', top: 36, left: -5 }}>
        <img src={require('../assets/remi0.png')} alt="Logo" className="logo-image" />
      </div>

      {/* Photo Grid */}
      <div className="photo-grid">
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt= "Photo 1" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 2" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 3" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 4" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 5" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 6" className="photo-grid-item" />
        <img src={require("../assets/tabitha-turner-Ns2aJ5OXKds-unsplash.jpg")} alt="Photo 7" className="photo-grid-item" />
      </div>

      {/* Upload Recipe Button */}
      <div className="upload-recipe-button-container" style={{ position: 'absolute', top: 522, left: 40 }}>
        <button className="button upload-recipe-button">upload recipe</button>
      </div>

      {/* Heading: Your Health in Your Hands */}
      <div className="heading-1" style={{ position: 'absolute', top: 649, left: 62, textAlign: 'center' }}>
        your health in your hands
      </div>

    </div>
  );
};

export default HomePage;