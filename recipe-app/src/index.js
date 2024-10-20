import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Outlet } from 'react-router-dom';

// import components
import FirstPage from './components/firstPage'; 
import MainForm from './components/mainForm';
import ScalingInput from './components/scaling'
import ProteinGoalInput from './components/proteinGoals';
import FinalSubmitButton from './components/finalSubmit';
import MainInput from "./components/mainInput";
import EmbedPage from "./components/embedPage";
import Loading from "./components/loading";
import Output from "./components/output";
import Navbar from "./components/navbar";
import HomePage from './components/HomePage'; 

function Layout() {
  return (
    <div>
      <Navbar />
      <Outlet />
    </div>
  );
}

export default function App() {
return (
  <BrowserRouter>
    <Routes>
      {/* Set Layout as the base route */}
      <Route path="/" element={<Layout />} >
        {/* Use 'index' for the default page */}
        <Route index element={<HomePage />} />
        <Route path="input" element={<MainInput />} />
        <Route path="embed" element={<EmbedPage />} />
        <Route path="form" element={<MainForm />} />
        <Route path="protein" element={<ProteinGoalInput />} />
        <Route path="scale" element={<ScalingInput />} />
        <Route path="load" element={<Loading />} />
        <Route path="output" element={<Output />} />
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
