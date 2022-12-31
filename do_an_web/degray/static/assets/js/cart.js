$(document).ready(function(){

    $(".qtyplus-cart").click(function (e) {
        // e.preventDefault();
        var number = $(this).parents(".item-qty").find(".line-item-qty").attr("value");
        if (number >= parseInt(1)){
            new_number = parseInt(number)+1;
            // alert(new_number);
            $(this).parents(".item-qty").find(".line-item-qty").val(new_number);
        }
    })

    $(".qtyminus-cart").click(function () {
        var number = $(this).parents(".item-qty").find(".line-item-qty").attr("value");
        if (number >= parseInt(2)){
            new_number = parseInt(number)-1;
            $(this).parents(".item-qty").find(".line-item-qty").val(new_number);
        }
        else {
            $(this).parents(".item-qty").find(".line-item-qty").val(number);
        }
    })
});
