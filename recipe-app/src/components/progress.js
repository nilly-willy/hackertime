
function Progress({ pvalue }) {
    return (
      <div className="App">
        <progress value={parseFloat(pvalue)} />
      </div>
    );
  }

export default Progress;





