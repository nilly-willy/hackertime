import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import reportWebVitals from './reportWebVitals';

// import components
import Progress from './components/progress';
import MainForm from './components/mainForm';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <h1>REMI</h1>
    <Progress/>
    <MainForm/>

  </React.StrictMode>
);

reportWebVitals();
