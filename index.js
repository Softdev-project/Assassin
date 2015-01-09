var myPos;
var map;

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

// To add the marker to the map, use the 'map' property
var marker = new google.maps.Marker({
    position: myLatlng,
    title:"Hello World!"
});

marker.setMap(map);

google.maps.event.addDomListener(window, 'load', initialize);
