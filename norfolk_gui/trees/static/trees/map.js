
let map;
async function initMap() {
    let lat_long_data = document.getElementById("data").value;

    const { Map } = await google.maps.importLibrary("maps");
    map = new Map(document.getElementById("map"), {
        center: { lat: 36.8477, lng: -76.2951},
        zoom: 15,
    });

    let parsed_data = JSON.parse(lat_long_data);
    //console.log(parsed_data);
    for (const tree in parsed_data) {
        //console.log(tree);
        const marker = new google.maps.Marker({
                position: {lat: parseFloat(parsed_data[tree].latitude), lng: parseFloat(parsed_data[tree].longitude)},
                map: map,
            });
    }

}

initMap();