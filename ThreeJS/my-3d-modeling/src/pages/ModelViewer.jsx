import { useParams } from "react-router-dom";
import { Canvas } from "@react-three/fiber";
import { OrbitControls } from "@react-three/drei";
import RotatingBox from "../models/rotatingBox";
import RiderBike from "../models/ridingBicycle";
import BicycleDemo from "../models/rideNewBike";

export default function ModelViewer() {
  const { modelId } = useParams();

  return (
    <Canvas camera={{ position: [0, 0, 5] }}>
      <ambientLight />
      <OrbitControls />
      {modelId === "cube" && (
        <mesh>
          <boxGeometry />
          <meshStandardMaterial color="hotpink" />
        </mesh>
      )}
      {modelId === "tree" && (
        <mesh>
          <coneGeometry args={[1, 2, 12]} />
          <meshStandardMaterial color="forestgreen" />
        </mesh>
      )}
      {modelId === "rotatingBox"} &&(
      <RotatingBox />)
      {modelId === "ridingBike"} &&(
      <RiderBike />
      {modelId === "rideNewBike"} &&(
      <BicycleDemo />
      )
    </Canvas>
  );
}
