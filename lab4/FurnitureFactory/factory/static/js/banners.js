const banners = document.querySelectorAll(".banner");
const interval_input = document.getElementById("rotation-interval");
var currentIndex = 0;
var ms = 5000;

function rotateBanners() {
    banners[currentIndex].hidden=true;
    currentIndex = (currentIndex + 1) % banners.length;
    banners[currentIndex].hidden=false;
}

var rotationTimer = setInterval(rotateBanners, ms);
if (document.hasFocus()) {
        rotateBanners();
}

window.addEventListener('blur', function () {
    clearInterval(rotationTimer);
});

function changeInterval(){
    let value = parseInt(interval_input.value);
    if(value && value > 0 && value < 10){
        ms = value*1000;
        clearInterval(rotationTimer);
        rotationTimer = setInterval(rotateBanners, ms);
    }
}