import NextButton from './nextButton';
import Progress from './progress';

function Output() {
    return (
      <div className="App">
        <Progress pvalue="1" />
        <h1 style={{fontFamily: 'Sarpanch'}}>Your New Recipe:</h1>
      </div>
      
    );
  }

export default Output;