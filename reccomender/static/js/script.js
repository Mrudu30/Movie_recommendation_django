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
})