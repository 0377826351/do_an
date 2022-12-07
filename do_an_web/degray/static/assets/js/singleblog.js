$('.listprod-owl').owlCarousel({
  loop: true,
  margin:10,
  nav:true,
  responsive:{
      0:{
          items:3
      },
      600:{
          items:5
      },
      1000:{
          items:5
      }
  }
})

$('.detail-item-owl').owlCarousel({
  loop: true,
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
          items:1
      }
  }
})