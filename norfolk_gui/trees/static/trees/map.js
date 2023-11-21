
let map;
async function initMap() {
    let data = document.getElementById("data").value;
    const { Map } = await google.maps.importLibrary("maps");
    map = new Map(document.getElementById("map"), {
        center: { lat: 36.8477, lng: -76.2951},
        zoom: 15,
    });

    let parsed_data = JSON.parse(data);

    for (const tree in parsed_data) {

        const myLatlng = {lat: parseFloat(parsed_data[tree].latitude), lng: parseFloat(parsed_data[tree].longitude)}
        const species = parsed_data[tree].species;
        const genus = parsed_data[tree].genus;
        const id = tree;
        const marker = new google.maps.Marker({
                position: myLatlng,
                map: map,
            });
        marker.addListener("click", () => {

            // initialize InfoWindow
            let infoWindow = new google.maps.InfoWindow({
                content: "Click to get event data",
                position: myLatlng,
            });

            // when use clicks, display content
            infoWindow = new google.maps.InfoWindow({
                position: myLatlng,
            });
            var displayMessage = "<p>ID: " + id + "</p>" + "<p>Species: " + species + "</p>" + "<p>Genus: " + genus + "</p>";
            infoWindow.setContent(displayMessage);
            infoWindow.open(map);
        });
    }

}

initMap();