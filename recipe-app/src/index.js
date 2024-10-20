import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Outlet } from 'react-router-dom';

// import components
import FirstPage from './components/firstPage'; 
import MainForm from './components/mainForm';
import Progress from './components/progress';

function Layout() {
  return (
    <div>
      <h1>REMI</h1>
    </div>
  );
}

export default function App() {
return (
  <BrowserRouter>
    <Routes>
      {/* Set Layout as the base route */}
      <Route path="/">
        {/* Use 'index' for the default page */}
        <Route index element={<FirstPage />} />
        <Route path="form" element={<MainForm />} />
        <Route path="progress" element={<Progress />} />
      </Route>
    </Routes>
  </BrowserRouter>
);
}
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
    <App />
);

// reportWebVitals();
