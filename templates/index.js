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
//controls.enabled = false;

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
        moveToCenter();
      });
});

var animate = function() {
    requestAnimationFrame(animate);
    controls.update();
    renderer.setClearColor(0xf3f7f0, 1);
    renderer.render(scene, camera);
};

var updateData = function() {
    fetch("http://localhost:5000/data")
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            // Update the DOM
            document.getElementById("data-a-x").innerHTML = data["a"]["x"];
            document.getElementById("data-a-y").innerHTML = data["a"]["y"];
            document.getElementById("data-a-z").innerHTML = data["a"]["z"];
            document.getElementById("data-o-pitch").innerHTML = data["o"]["pitch"];
            document.getElementById("data-o-roll").innerHTML = data["o"]["roll"];
            document.getElementById("data-o-yaw").innerHTML = data["o"]["yaw"];

            cad_obj.rotation.set(data["o"]["pitch"] - Math.PI/2, data["o"]["yaw"], data["o"]["roll"]);
            moveToCenter();
        })
        .catch(function() {
            console.log("Error occured with data request");
        });
};

function moveToCenter(){
  var children = cad_obj.children,
  completeBoundingBox = new THREE.Box3(); // create a new box which will contain the entire values
  completeBoundingBox = completeBoundingBox.setFromObject(cad_obj);
  var objectCenter = completeBoundingBox.center()

  cad_obj.position.x -= objectCenter.x;
  cad_obj.position.y -= objectCenter.y;
  cad_obj.position.z -= objectCenter.z;
}

animate();
setInterval(updateData, 5);
