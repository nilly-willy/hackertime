import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';

import reportWebVitals from './reportWebVitals';

// import components
import MainInput from './components/mainInput';
import Progress from './components/progress';
import MainForm from './components/mainForm';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Progress />
    <MainInput />
    <MainForm />


  </React.StrictMode>
);

reportWebVitals();
