// Function to reverse geocode using the Flask server
function reverseGeocode(lat, lon) {
    var url = `/reverse-geocode?lat=${lat}&lon=${lon}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.neighborhood) {
                alert("You are in the neighborhood of " + data.neighborhood);
            } else {
                alert("Neighborhood not found.");
            }
        })
        .catch(error => console.log('Error:', error));
}
// Function to get user's geolocation
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError, { enableHighAccuracy: true });
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
