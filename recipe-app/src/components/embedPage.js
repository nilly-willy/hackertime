import NextButton from './nextButton';
import Progress from './progress';

function EmbedPage() {
    return (
      <div className="App">
        <Progress pvalue="0.167" />
        <h1>nilly is making an image</h1>
        <NextButton to="/form" />
      </div>
    );
  }

export default EmbedPage;
