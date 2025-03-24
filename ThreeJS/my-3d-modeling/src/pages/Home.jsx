import { Link } from "react-router-dom";

export default function Home() {
  return (
    <div style={{ padding: 20 }}>
      <h1>Welcome to the 3D World 🌐</h1>
      <p>Click the <Link to='/gallery'>gallery</Link> to explore!</p>
    </div>

  );
}
