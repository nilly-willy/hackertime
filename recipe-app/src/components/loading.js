import NextButton from './nextButton';
import Progress from './progress';

function Loading() {
    return (
      <div className="App">
        <Progress pvalue="0.75" />
        <h1>LOADING RATSSSS into ur house</h1>
        <NextButton to="/output" />
      </div>
    );
  }

export default Loading;