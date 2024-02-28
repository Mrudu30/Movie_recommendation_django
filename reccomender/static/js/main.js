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
function edit_comment(id){
    var edit_id = parseInt(id)
    var edit_comment_id = "comment_"+edit_id
    // $('#'+edit_comment_id).
}