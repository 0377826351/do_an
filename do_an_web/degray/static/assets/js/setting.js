$(document).ready(function(){
    $(".svg-ico-cart").click(function () {
        $(".header-action-dropdown").addClass("active");
        
    });

    // $(".qtyplus-cart").click(function () {
    //     var number = document.getElementById("quantity").value;
    //     alert(number)
    //     if (number >= parseInt(0)){
    //         new_number = parseInt(number)+1;
    //         document.getElementById("quantity").value = new_number;
    //     }
    // })

    // $(".qtyminus-cart").click(function () {
    //     var number = document.getElementById("quantity").value;
    //     if (number >= parseInt(1)){
    //         new_number = parseInt(number)-1;
    //         document.getElementById("quantity").value = new_number;
    //     }
    // })

    $(".icon-bars").click(function () {
        $(this).children('i').toggleClass("fa-times").toggleClass("fa-bars");
        $("body").toggleClass("open-menu");
    });

    $('.opbg-mb').click(function(e) {
        $("body").removeClass("open-menu");
        $(this).parents().find(".icon-bars i").removeClass("fa-times").addClass("fa-bars");
    });

    $(".price-number").toLocaleString() 

    $(".search-header").click(function () {
        $(".opbg").css("visibility", "visible");
        $(document).mouseup(function(e) 
        {
            var container = $(".popup-search");
            if (!container.is(e.target) && container.has(e.target).length === 0) 
            {
                $(".opbg").css("visibility", "hidden");
            }
        });
    });
    
    $(".close-pop").click(function () {
        $(".opbg").css("visibility", "hidden");
    });

    if ($(".item-name").click(function(e) {
        e.preventDefault();
        $(this).children('i').toggleClass("fa-plus").toggleClass("fa-minus");
        if (!$(this).parent().hasClass('active')) {
            $(this).parents('.list-item').find('.item-item.active .item-content').slideUp("fast");
            $(this).parents('.list-item').find('.item-item.active .item-name').children("i").removeClass("fa-minus").addClass("fa-plus");
            $(this).parents('.list-item').find('.item-item.active').removeClass('active');
            $(this).parent().addClass('active');
            $(this).parent().find('.item-content').slideDown("fast");
        }else {
            $(this).parent().removeClass('active');
            $(".item-content").slideUp("fast");
        }
    }));

    if ($(".cart").click(function(e) {
        e.preventDefault();
        if (!$(this).parent().hasClass('active')) {
            $(this).parent().find('.cart-detail').toggle();
        }
    }));
});

$('.lisprod-item').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

$('.home-banner').owlCarousel({
    loop:true,
    margin:10,
    nav:true,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:1
        },
        1000:{
            items:1
        }
    }
})

