let video;
function setup() {
 createCanvas(windowWidth, windowHeight, WEBGL); // Usar WEBGL para objetos 3D
 video = createCapture(VIDEO);
 video.size(windowWidth, windowHeight);
 video.hide();
}
function draw() {
 background(255);

 // Mostrar la imagen de la cámara
 push();
 translate(-windowWidth / 2, -windowHeight / 2); // Posicionar imagen
 image(video, 0, 0, windowWidth, windowHeight);
 pop();

 // Simulación de Realidad Aumentada con objetos 3D
 push();
 rotateY(millis() / 1000);
 rotateX(millis() / 2000);
 noFill();
 stroke(255, 0, 0);
 box(100);
 pop();

 // Añadir más objetos o efectos que interactúan con el ratón
 push();
 fill(0, 0, 255, 150);
 noStroke();
 translate(mouseX - width / 2, mouseY - height / 2, 0);
 sphere(50); // Esfera que sigue al ratón
 pop();
}
function windowResized() {
 resizeCanvas(windowWidth, windowHeight);
}
