"use strict"; 

var map;

function initialize() {
    debugger;
    var mapOptions = {
        zoom: 15
    };
    map = new google.maps.Map(
            $('#map-canvas'),
            mapOptions);

    // Try HTML5 geolocation
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {

            var pos = new google.maps.LatLng(
                    position.coords.latitude,
                    position.coords.longitude);

            // var marker = new google.maps.Marker({
            //         position: pos,
            //         map: map,
            // });                

            var infowindow = new google.maps.InfoWindow({
                position: pos,
                map: map,
                content: 'You are here!'
            });

            map.setCenter(pos);
        }, function () {
            handleNoGeolocation(true);
        });
    } else {
        // Browser doesn't support Geolocation
        handleNoGeolocation(false);
    }
}

function handleNoGeolocation(errorFlag) {
    var content;

    if (errorFlag) {
        content = "Error: The Geolocation service failed.";
    } else {
        content = "Error: Your browser doesn't support geolocation.";
    }

    var options = {
        map: map,
        position: new google.maps.LatLng(60, 105),
        content: content
    };

    var infowindow = new google.maps.InfoWindow(options);
    map.setCenter(options.position);
}

