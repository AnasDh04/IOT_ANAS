// Initialize the map
var mymap = L.map('map').setView([51.505, -0.09], 13);

// Add a tile layer to the map
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(mymap);

// Add a marker to the map
var marker = L.marker([51.5, -0.09]).addTo(mymap);

// Add a popup to the marker
marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup();
