import { SelectButton } from 'primereact/selectbutton';
import React, { useState } from "react";

function MainForm() {
    const options = ['Diabetes', 'Pregnancy', 'PCOS', 'Celiacs Disease', 'Heart Disease'];
    const [value, setValue] = useState(options[0]);
    
    return (
      <div className="mainForm">
            <SelectButton value={value} onChange={(e) => setValue(e.value)} options={options} />
      </div>
    );
  }

export default MainForm;