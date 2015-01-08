var myPos;
var map;
function initialize() {    
    var mapOptions = {
	zoom: 20	
    };
    map = new google.maps.Map(document.getElementById('map-canvas'),
				  mapOptions);
    
    if(navigator.geolocation) {
	browserSupportFlag = true;
	navigator.geolocation.getCurrentPosition(function(position) {
	    initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
	    myPos = initialLocation;
	    map.setCenter(initialLocation);
	}, function() {
	    handleNoGeolocation(browserSupportFlag);
	});
    }

    else {
	browserSupportFlag = false;
	handleNoGeolocation(browserSupportFlag);
    }
}

var marker = new google.maps.Marker({
    position: myPos,
    map: map,
    title:"Hello World!"
});

google.maps.event.addDomListener(window, 'load', initialize);
marker.setMap(map);
