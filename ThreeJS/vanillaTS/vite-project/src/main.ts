import * as THREE from 'three';
import { Wheel } from './components/Wheel';

// Create scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0xeeeeee);

// Create camera
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.set(0, 5, 10);

// Create renderer
const renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.shadowMap.enabled = true;
document.body.appendChild(renderer.domElement);

// Add light
const light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(5, 10, 5);
light.castShadow = true;
scene.add(light);

// wheel position

// Create and add wheels
const wheel1 = new Wheel(-3, 0, 0);
const wheel2 = new Wheel(3, 0, 0);

scene.add(wheel1.mesh);
scene.add(wheel2.mesh);

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  wheel1.rotate();
  wheel2.rotate();
  renderer.render(scene, camera);
}

animate();

// Handle window resize
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
