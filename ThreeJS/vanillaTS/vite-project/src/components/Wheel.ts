import * as THREE from "three";

export class Wheel {
  public mesh: THREE.Mesh;

  constructor(x: number, y: number, z: number) {
    const geometry = new THREE.TorusGeometry(1, 0.1, 16, 100);
    const material = new THREE.MeshStandardMaterial({ color: 0x000000 });

    this.mesh = new THREE.Mesh(geometry, material);
    this.mesh.position.set(x, y, z);
    this.mesh.castShadow = true;
    this.mesh.receiveShadow = true;
  }

  rotate(speed: number = 0.01) {
    this.mesh.rotation.x += speed;
  }
}
