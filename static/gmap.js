"use strict";
    var map;
    function initMap() {
        map = new google.maps.Map(document.getElementById('sf-map'), {
            center: {lat: 37.7749, lng: -122.4194},
            zoom: 12
        });

        $.get('/get_markers.json', mapMarkers);

    }


    function mapMarkers(data) {

        for (var food_truck in data) {
            var infoWindow = new google.maps.InfoWindow();

            let value = data[food_truck];
            var marker = new google.maps.Marker({
                position: new google.maps.LatLng(value['lat'], value['long']),
                map: map,
            });
            console.log(marker);

            marker.addListener('click', function(){
                addWindow(this, infoWindow, value)
            })
        }
    }
    function addWindow(marker, infoWindow, data) {
        if (infoWindow.marker != marker) {
            infoWindow.marker = marker;
            infoWindow.setContent('<div class="map-pin"><p>Name: ' + data.name + '</p><p>Latitude: ' + data.lat + '</p><p>Longitude: ' + data.long + '</p></div>');
            infoWindow.open(map, marker)

            infoWindow.addListener('closeclick', function(){
                infoWindow.setMarker(null)
            })
        }

    }

