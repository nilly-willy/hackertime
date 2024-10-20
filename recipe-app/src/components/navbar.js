import React, { useState } from 'react';
import '../Navbar.css'; 

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  const toggleMenu = () => {
    console.log(isOpen)
    setIsOpen(!isOpen);
  };

  return (
    <nav className="navbar-n">
      {/* Logo Section */}
      <div className="logo-n">
        <img src={require('../assets/remi1.png')} alt="Logo" /> 
      </div>

      {/* Hamburger Menu Icon */}
      <div className="hamburger-n" onClick={toggleMenu}>
        <span className="line-n"></span>
        <span className="line-n"></span>
        <span className="line-n"></span>
      </div>

      {/* Navigation Menu */}
      <ul className={`menu-n ${isOpen ? 'open' : ''}`}>
        <li className="menuli-n"><a href="#home">Home</a></li>
        <li className="menuli-n"><a href="#about">Recipes</a></li>
        <li className="menuli-n"><a href="#services">About</a></li>
      </ul>
    </nav>
  );
};

export default Navbar;
