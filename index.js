
var showposition = function(p){
    var x = document.getElementById("demo");
    x.innerHTML = "Lat: "+p.coords.latitude+"<br>Long: "+p.coords.longitude+"<br>Alt: " + p.coords.altitude;
}

var go = function() {
    if ("geolocation" in navigator){
	console.log("Geolocation");
	navigator.geolocation.getCurrentPosition(initialize);
    } else {
	console.log("No Geolocation");
    }
}

//DO THING WITH THE ONLOAD THING HELP PLS THANKA
window.onLoad = go;
