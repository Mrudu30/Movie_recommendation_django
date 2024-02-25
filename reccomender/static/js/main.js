$(document).ready(function () {
    
    $("#search").on("keyup",function(){
        var data = {'q': $(this).val()};
        $.ajax({
            type: "GET",
            url: "{% url 'home' %}",
            data: data,
            success: function (response) {
                console.log("successfully sent")
            }
        });
    })

});