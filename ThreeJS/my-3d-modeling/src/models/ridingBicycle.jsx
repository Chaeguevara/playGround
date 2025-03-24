import { Canvas, useFrame } from '@react-three/fiber'
import { OrbitControls } from '@react-three/drei'
import { useRef } from 'react'

export default function Bicycle() {
  const frontWheel = useRef()
  const rearWheel = useRef()
  const crank = useRef()
  const leftLeg = useRef()
  const rightLeg = useRef()
  const bikeGroup = useRef()

  useFrame(({ clock }) => {
    const t = clock.getElapsedTime()
    const pedalRotation = t * 2 * Math.PI * 0.5 // 0.5 rotations per second

    // Wheels rotate clockwise
    frontWheel.current.rotation.x = -pedalRotation
    rearWheel.current.rotation.x = -pedalRotation

    // Crank rotates
    crank.current.rotation.z = pedalRotation

    // Legs follow the pedal position
    const radius = 0.3
    const speed = 2
    leftLeg.current.position.y = Math.sin(pedalRotation) * radius
    rightLeg.current.position.y = Math.sin(pedalRotation + Math.PI) * radius
  })

  return (
    <group ref={bikeGroup}>
      {/* Frame */}
      <mesh position={[0, 0.5, 0]}>
        <boxGeometry args={[2, 0.1, 0.1]} />
        <meshStandardMaterial color="gray" />
      </mesh>

      {/* Wheels */}
      <mesh ref={frontWheel} position={[1, 0, 0]} rotation={[0, 0, 0]}>
        <torusGeometry args={[0.4, 0.05, 16, 100]} />
        <meshStandardMaterial color="black" />
      </mesh>
      <mesh ref={rearWheel} position={[-1, 0, 0]} rotation={[0, 0, 0]}>
        <torusGeometry args={[0.4, 0.05, 16, 100]} />
        <meshStandardMaterial color="black" />
      </mesh>

      {/* Crank */}
      <mesh ref={crank} position={[-0.3, 0.3, 0]} rotation={[0, 0, 0]}>
        <cylinderGeometry args={[0.02, 0.02, 0.4, 32]} />
        <meshStandardMaterial color="silver" />
      </mesh>

      {/* Legs */}
      <mesh ref={leftLeg} position={[-0.3, 0.3, 0.1]}>
        <boxGeometry args={[0.1, 0.5, 0.1]} />
        <meshStandardMaterial color="blue" />
      </mesh>
      <mesh ref={rightLeg} position={[-0.3, 0.3, -0.1]}>
        <boxGeometry args={[0.1, 0.5, 0.1]} />
        <meshStandardMaterial color="blue" />
      </mesh>
    </group>
  )
}
