document.getElementsByClassName("remove").item(0).addEventListener("click",
    ()=>{
    document.getElementsByClassName("no-image").item(0)
        .innerHTML="<img src='/images/user-imageVas/user.png'>";

    document.getElementsByClassName("input-img").item(0).value="";
})



function validateName(index){
    let name = document.getElementsByClassName('text-input').item(index).value;
    if (name===""){
        document.getElementsByClassName("fas fa-bicycle fa-xs").item(index).style.color="#e53e3e";
    } else {
        document.getElementsByClassName("fas fa-bicycle fa-xs").item(index).style.color="#71cc35";
    }
}

function validatePrice(){
    const pattern = "^[0-9]{10}$"
    let phone = document.getElementById('rate').value;
    if (!phone.match(pattern)){
        document.getElementsByClassName("fas fa-money-bill fa-xs fa-flip-horizontal").style.color="#e53e3e";
    } else {
        document.getElementsByClassName("fas fa-money-bill fa-xs fa-flip-horizontal").style.color="#71cc35";
    }
}

function validateCategory(){
    var card = document.getElementById("bike_type")[0].value;
    if (!card.value == biketype) {
        document.getElementsByClassName("fas fa-bicycle fa-xs fa-flip-horizontal").style.color="#e53e3e";
    } else {
        document.getElementsByClassName("fas fa-bicycle fa-xs fa-flip-horizontal").style.color="#71cc35";
    }

}

function validateCategory(){
    var card = document.getElementById("bike_type")[0].value;
    if (!card.value == biketype) {
        document.getElementsByClassName("fas fa-bicycle fa-xs fa-flip-horizontal").style.color="#e53e3e";
    } else {
        document.getElementsByClassName("fas fa-bicycle fa-xs fa-flip-horizontal").style.color="#71cc35";
    }

}

function validateAvailablity(){
    
    var card = document.getElementById("availablity")[0].value;
    if (!card.value == availablity) {
        document.getElementsByClassName("fas fa-person-biking fa-xs fa-flip-horizontal").style.color="#e53e3e";
    } else {
        document.getElementsByClassName("fas fa-person-biking fa-xs fa-flip-horizontal").style.color="#71cc35";
    }

}

function addImages(){
        var input = document.getElementById("image");
        var img = document.getElementById("ItemPreview");
      console.log("REACHED ");
        img.src = URL.createObjectURL(input.files[0]);
      
}


function addImage(){
    let fileInput = document.getElementsByClassName("input-img").item(0);
    let filePath = fileInput.value;

    console.log(filePath);

    const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;

    if (filePath===""){
        document.getElementsByClassName("remove").item(0)
    }

    console.log("1");

    if (!allowedExtensions.exec(filePath)) {
        document.getElementsByClassName('picture').item(1).style.border="2px solid #e94d4d";
    } else {
        document.getElementsByClassName('picture').item(1).style.border="2px solid white";
    }
    
    console.log("2");

    document.getElementsByClassName("no-image").item(0)
        .innerHTML = "<img src='" + URL.createObjectURL(event.target.files[0]) + "' alt='Profile Picture'>"
}

// send data to server
function sendData(){
    console.log("sendData");
    let name = document.getElementById('company_name').value;
    let description = document.getElementById('bike_type').value;
    let price = document.getElementById('rate').value;
    // let fileInput = document.getElementById("input-img");

    console.log(name, description, price);
    navigator.geolocation.getCurrentPosition(function(position) {
        location = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

    let data = {
        name: name,
        description: description,
        price: price,
        //image: filePath
        location: location,
        csrfmiddlewaretoken: '{{csrf_token}}'
    }
    console.log(data);
    $.ajax({
        type: "POST",
        url: '/add_cycle',
        data: data,
        success: function(response) {
            console.log(response);
        },
        error: function(error) {
            console.log(error);
        }
    });
}
)}