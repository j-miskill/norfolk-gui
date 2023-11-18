
let map;
async function initMap() {
    const { Map } = await google.maps.importLibrary("maps");
    map = new Map(document.getElementById("map"), {
        center: { lat: 36.88809, lng: -76.28566},
        zoom: 15,
    });
}

initMap();