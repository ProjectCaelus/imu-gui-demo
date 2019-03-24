var scene = new THREE.Scene();

var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
camera.position.z = 200;

var renderer = new THREE.WebGLRenderer();
renderer.setSize(window.innerWidth, window.innerHeight);
document.body.appendChild(renderer.domElement);

var controls = new THREE.OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;
controls.enabled = false;

var keyLight = new THREE.DirectionalLight(new THREE.Color("hsl(30, 100%, 75%)"), 1.0);
keyLight.position.set(-100, 0, 100);

var fillLight = new THREE.DirectionalLight(new THREE.Color("hsl(240, 100%, 75%)"), 0.75);
fillLight.position.set(100, 0, 100);

var backLight = new THREE.DirectionalLight(0xffffff, 1.0);
backLight.position.set(100, 0, -100).normalize();

scene.add(keyLight);
scene.add(fillLight);
scene.add(backLight);

var cad_obj;

var mtlLoader = new THREE.MTLLoader();
mtlLoader.setTexturePath("../assets/stl/");
mtlLoader.setPath("../assets/stl/");
mtlLoader.load("./callisto.mtl", function(materials) {
    materials.preload();

    var objLoader = new THREE.OBJLoader();
    objLoader.setMaterials(materials);
    objLoader.setPath("../assets/stl/");
    objLoader.load("./callisto.obj", function(object) {
        cad_obj = object;
        scene.add(object);
        object.scale.set(0.1, 0.1, 0.1);
        object.rotation.set(-Math.PI / 2, 0, 0);
        object.position.y -= 80;
    });
});

var animate = function() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.setClearColor(0xbbbbbb, 1);
    renderer.render(scene, camera);
};

animate();
