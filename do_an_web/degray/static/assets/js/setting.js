$(document).ready(function(){
    $(".svg-ico-cart").click(function () {
        $(".header-action-dropdown").addClass("active");
        
    });

    $(".icon-bars").click(function () {
        $(this).children('i').toggleClass("fa-times").toggleClass("fa-bars");
        $("body").toggleClass("open-menu");
    });

    $('.opbg-mb').click(function(e) {
        $("body").removeClass("open-menu");
        $(this).parents().find(".icon-bars i").removeClass("fa-times").addClass("fa-bars");
    });

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



