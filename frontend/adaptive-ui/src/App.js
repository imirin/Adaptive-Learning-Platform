import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then(res => res.json())
      .then(data => setMessage(data.message))
      .catch(() => setMessage("Backend not connected"));
  }, []);

  return (
    <div style={{ padding: "40px", fontSize: "20px" }}>
      <h1>Adaptive Learning Platform</h1>
      <p>Backend says: {message}</p>
    </div>
  );
}

export default App;
