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
        $(".search").toggleClass('search-open')
    })
    $('.movie-loop').slick({
        dots: false,
        infinite: true,
        speed: 300,
        slidesToShow: 5,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 2000,
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
