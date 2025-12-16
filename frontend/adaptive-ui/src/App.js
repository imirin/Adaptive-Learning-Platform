import { useState } from "react";

function App() {
  const [scores, setScores] = useState({ python: "", dsa: "", ai: "" });
  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setScores({ ...scores, [e.target.name]: Number(e.target.value) });
  };

  const submitAssessment = () => {
    fetch("http://127.0.0.1:8000/api/assess-skill", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(scores),
    })
      .then((res) => res.json())
      .then((data) => setResult(data));
  };

  return (
    <div style={{ padding: "40px" }}>
      <h1>Adaptive Learning Platform</h1>

      <h2>Skill Assessment</h2>

      <input
        type="number"
        name="python"
        placeholder="Python Skill (0-100)"
        onChange={handleChange}
      /><br /><br />

      <input
        type="number"
        name="dsa"
        placeholder="DSA Skill (0-100)"
        onChange={handleChange}
      /><br /><br />

      <input
        type="number"
        name="ai"
        placeholder="AI Skill (0-100)"
        onChange={handleChange}
      /><br /><br />

      <button onClick={submitAssessment}>Assess</button>

      {result && (
        <>
          <h3>Level: {result.level}</h3>
          <h4>Recommended Path:</h4>
          <ul>
            {result.recommended_path.map((topic, i) => (
              <li key={i}>{topic}</li>
            ))}
          </ul>
        </>
      )}
    </div>
  );
}

export default App;
