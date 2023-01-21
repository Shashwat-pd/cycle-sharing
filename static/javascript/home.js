$(document).ready(function() {
  navigator.geolocation.getCurrentPosition(function(position) {
    var data = {
      lat: position.coords.latitude,
      lng: position.coords.longitude
    };
    console.log("thisssssss")
    $.ajax({
      type: 'POST',
      url: '/get_position',
      data: data,
      success: function(response) {
        console.log(response);
      },
      error: function(error) {
        console.log(error);
      }
    });
  });
});
