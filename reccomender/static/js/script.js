$(document).ready(function(){
    $(".toggler-button").on( 'click' , function(){
        $(".offcanvas").toggleClass('show')
        $(".offcanvas").css("visibility", "visible")
    })
    $(".btn-close").click(function(){
        $(".offcanvas").removeClass('show')
        $(".offcanvas").css("visibility", "hidden")
    })
    $(".toggler-search-icon").click(function(){
        $(".search").css('display' , "block")
    })
    $('.movie-loop').slick({
        dots: false,
        infinite: false,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 5,
        responsive: [
          {
            breakpoint: 1024,
            settings: {
              slidesToShow: 3,
              slidesToScroll: 3,
              infinite: true,
              dots: true
            }
          },
          {
            breakpoint: 600,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 480,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
        ]
      });
})
