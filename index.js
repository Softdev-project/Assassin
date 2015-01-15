var initialLocation;
var siberia = new google.maps.LatLng(60, 105);
var newyork = new google.maps.LatLng(40.69847032728747, -73.9514422416687);
var browserSupportFlag =  new Boolean();

var init = function initialize() {
    var myOptions = {
	zoom: 6,
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);
    
    if(navigator.geolocation) {
	browserSupportFlag = true;
	navigator.geolocation.getCurrentPosition(function(position) {
	    initialLocation = new google.maps.LatLng(position.coords.latitude,position.coords.longitude);
	    map.setCenter(initialLocation);
	    
	    var myLatlng = initialLocation;
	    var myMarker = new google.maps.Marker({
		position: myLatlng,
		map: map,
		title:"Hello World!"
	    });

	    var targetLatLng = new google.maps.LatLng(position.coords.latitude + 0.05, position.coords.longitude + 0.05);
	    var targetMarker = new google.maps.Marker({
		position: targetLatLng,
		map: map,
		title:"Hello World!"
	    });
	    
	}, function() {
	    handleNoGeolocation(browserSupportFlag);
	});
    }
    else {
	browserSupportFlag = false;
	handleNoGeolocation(browserSupportFlag);
    }
    
    function handleNoGeolocation(errorFlag) {
	if (errorFlag == true) {
	    alert("Geolocation service failed.");
	    initialLocation = newyork;
	} else {
	    alert("Your browser doesn't support geolocation. We've placed you in Siberia.");
	    initialLocation = siberia;
	}
	map.setCenter(initialLocation);
    }
}

window.onLoad = init();
