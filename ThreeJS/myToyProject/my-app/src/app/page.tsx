"use client"
import Image from "next/image";
import styles from "./page.module.css";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import { Suspense, useRef } from "react";
import { Preload, Image as ImageImpl } from "@react-three/drei";
import { ScrollControls, useScroll } from "@react-three/drei";
import * as THREE from "three";

function ImageLoader(props) {
  const ref = useRef()
  const group = useRef()
  const data = useScroll()
  useFrame((state, delta) => {
    group.current.position.z = THREE.MathUtils.damp(group.current.position.z, Math.max(0, data.delta * 50), 4, delta)
    ref.current.material.grayscale = THREE.MathUtils.damp(ref.current.material.grayscale, Math.max(0, 1 - data.delta * 1000), 4, delta)
  })
  return (
    <group ref={group}>
      <ImageImpl ref={ref} {...props} />
    </group>
  )

}

function Page({ m = 0.4, urls, ...props }) {
  const { width } = useThree((s) => s.viewport)
  const w = width < 10 ? 1.5 / 3 : 1 / 3
  return (
    <group {...props}>
      <ImageLoader position={[-width * w, 0, -1]} scale={[width * w - m * 2, 5, 1]} url={urls[0]} />
      <ImageLoader position={[0, 0, 0]} scale={[width * w - m * 2, 5, 1]} url={urls[1]} />
      <ImageLoader position={[-width * w, 0, 1]} scale={[width * w - m * 2, 5, 1]} url={urls[2]} />
    </group>
  )
}

function Pages() {
  const { width } = useThree((state) => state.viewport)
  return (
    <>
      <Page position={[-width * 1, 0, 0]} urls={['../../public/hi.jpeg','../../public/hi.jpeg','../../public/hi.jpeg']} />

    </>
  )
}

export default function Home() {
  return (
    <main>
      <Canvas gl={{ antialias: false }} dpr={[1, 1.5]}>
        <Suspense fallback={null}>
          <ScrollControls infinite horizontal damping={4} pages={4} distance={1}>
            <Pages />

          </ScrollControls>
        </Suspense>

      </Canvas>

    </main>
  );
}
