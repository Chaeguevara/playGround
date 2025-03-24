import { Link } from "react-router-dom";

const models = [
  { id: "cube", name: "Cube" },
  { id: "tree", name: "Tree" },
  { id: "rotatingBox", name: "RotatingBox" },
  { id: "ridingBike", name: "Riding Bicycle" },
  { id: "rideNewBike", name: "Riding New Bicycle" },
];

export default function Gallery() {
  return (
    <div style={{ padding: 20 }}>
      <h2>Select a Model</h2>
      <ul>
        {models.map((model) => (
          <li key={model.id}>
            <Link to={`/gallery/${model.id}`}>{model.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
}
