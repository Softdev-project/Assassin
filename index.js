var myPos;
var map;
/*
function initialize(){
    var mapOptions = {
	zoom: 15	
    };
    map = new google.maps.Map(document.getElementById('map-canvas'),
				  mapOptions);
    if(navigator.geolocation) {
	browserSupportFlag = true;
	navigator.geolocation.getCurrentPosition(function(position) {
	    myPos = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
	    map.setCenter(myPos);
	}, function() {
	    handleNoGeolocation(browserSupportFlag);
	});
    }

    else {
	browserSupportFlag = false;
	handleNoGeolocation(browserSupportFlag);
    }
}

var myLatlng = new google.maps.LatLng(-25.363882,131.044922);


var marker = new google.maps.Marker({
    position: myLatlng,
    title:"Hello World!",
    map: map,
    visible: true
});
console.log(marker.position);
*////////
/*
var markerme;
function initialize() {
    latLng = new google.maps.LatLng(-8.064903, -34.896872)
    var mapOptions = {
	center: latLng,
	zoom: 16,
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), mapOptions);
    
    markerme = new google.maps.Marker({
	position: latLng,
	title:"Hello World!",
	visible: true,
	map: map
    });
}

var markerset = function markerset(marker){
    console.log("markers????");
    var new_marker_position = new google.maps.LatLng(marker.position.lat()+5, marker.position.lng+5);
    marker.setPosition(new_marker_position);
    console.log(marker.position.lat());
}

var meset = function(){
    markerset(markerme);
    markerme.visible = true;
}

google.maps.event.addDomListener(window, 'load', initialize());
window.setInterval(meset, 3000);

*/
var marker;
$(window).load(function() {
    myOptions = { 
	zoom: 20,
	mapTypeId: google.maps.MapTypeId.ROADMAP 
    };
    map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    var watchId = navigator.geolocation.watchPosition(centerMap); 
    var myLatlng = new google.maps.LatLng(location.coords.latitude,location.coords.longitude);
    marker = new google.maps.Marker({
	position: myLatlng,
	map: map,
	zIndex:1
    });
});

function centerMap(location)
{
    var myLatlng = new google.maps.LatLng(location.coords.latitude,location.coords.longitude);
    map.setCenter(myLatlng);
    map.setZoom(15);
    
    $("#lat").text("Latitude : " + location.coords.latitude);
    $("#lon").text("Longitude : " + location.coords.longitude);
 
   //show current location on map
    marker.setPosition(myLatlng);
}
