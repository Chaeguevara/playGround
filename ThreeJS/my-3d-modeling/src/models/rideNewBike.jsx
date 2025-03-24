import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls } from '@react-three/drei';
import * as THREE from 'three';

function PedalCrank({ crankRef, pedalLeftRef, pedalRightRef }) {
  useFrame((state, delta) => {
    crankRef.current.rotation.z -= delta * 2; // crank rotation
  });

  return (
    <group ref={crankRef}>
      <mesh ref={pedalLeftRef} position={[0, -0.6, 0]}>
        <boxGeometry args={[0.1, 0.2, 0.1]} />
        <meshStandardMaterial color="blue" />
      </mesh>
      <mesh ref={pedalRightRef} position={[0, 0.6, 0]}>
        <boxGeometry args={[0.1, 0.2, 0.1]} />
        <meshStandardMaterial color="blue" />
      </mesh>
      <cylinderGeometry args={[0.05, 0.05, 1.2, 32]} />
    </group>
  );
}

function Chainring({ crankRef }) {
  return (
    <mesh position={[1, 0, 0]} rotation={[0, 0, 0]}>
      <torusGeometry args={[0.4, 0.05, 16, 100]} />
      <meshStandardMaterial color="gray" />
    </mesh>
  );
}

function RearWheel({ wheelRef }) {
  useFrame((state, delta) => {
    wheelRef.current.rotation.x -= delta * 4; // Adjust according to gear ratio
  });

  return (
    <mesh ref={wheelRef} position={[3, 0, 0]} rotation={[0, 0, 0]}>
      <torusGeometry args={[0.6, 0.1, 16, 100]} />
      <meshStandardMaterial color="black" />
    </mesh>
  );
}

function Rider({ pedalLeftRef, pedalRightRef }) {
  const leftLegRef = useRef();
  const rightLegRef = useRef();

  useFrame(() => {
    leftLegRef.current.rotation.x = Math.sin(pedalLeftRef.current.getWorldPosition(new THREE.Vector3()).y * Math.PI);
    rightLegRef.current.rotation.x = Math.sin(pedalRightRef.current.getWorldPosition(new THREE.Vector3()).y * Math.PI);
  });

  return (
    <group position={[0, 1, 0]}>
      <mesh position={[0, 1, 0]}>
        <boxGeometry args={[0.4, 0.4, 0.2]} />
        <meshStandardMaterial color="peachpuff" />
      </mesh>
      <group ref={leftLegRef} position={[0, 0.6, -0.1]}>
        <mesh position={[0, -0.3, 0]}>
          <boxGeometry args={[0.1, 0.6, 0.1]} />
          <meshStandardMaterial color="peachpuff" />
        </mesh>
      </group>
      <group ref={rightLegRef} position={[0, 0.6, 0.1]}>
        <mesh position={[0, -0.3, 0]}>
          <boxGeometry args={[0.1, 0.6, 0.1]} />
          <meshStandardMaterial color="peachpuff" />
        </mesh>
      </group>
    </group>
  );
}

export default function BicycleDemo() {
  const crankRef = useRef();
  const pedalLeftRef = useRef();
  const pedalRightRef = useRef();
  const wheelRef = useRef();

  return (

    <>
      <PedalCrank crankRef={crankRef} pedalLeftRef={pedalLeftRef} pedalRightRef={pedalRightRef} />
      <Chainring crankRef={crankRef} />
      <RearWheel wheelRef={wheelRef} />
     <Rider pedalLeftRef={pedalLeftRef} pedalRightRef={pedalRightRef} />
     </>
  );
}
