$(document).ready(function(){
    $(".qtyplus").click(function () {
        var number = document.getElementById("qty-item").value;
        if (number >= parseInt(0)){
            new_number = parseInt(number)+1;
            document.getElementById("qty-item").value = new_number;
        }
    })

    $(".qtyminus").click(function () {
        var number = document.getElementById("qty-item").value;
        if (number >= parseInt(1)){
            new_number = parseInt(number)-1;
            document.getElementById("qty-item").value = new_number;
        }
    })
});