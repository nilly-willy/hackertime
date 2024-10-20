import '../index.css';
import NextButton from './nextButton';

function FirstPage() {
    return (
      <div className="heading-1">
        <h1>OH YEAHH cool app coming soon</h1>
        <NextButton to="/input" />
      </div>
    );
  }

export default FirstPage;

