var csrfToken = getCSRFToken();
$(document).ready(function () {
    console.log("jquery loaded")
    $("#search").on("keyup",function(){
        $.ajax({
            type: "POST",
            headers: {
                'X-CSRFToken': csrfToken
            },
            url: "/home/",
            data: ("#searchform").serialize,
            success: function (response) {
                console.log("successfully sent")
            }
        });
    })

});

function edit_comment(id){
    var edit_id = parseInt(id)
    var edit_comment_id = "comment_"+edit_id
    $("#editCommentDiv_"+edit_id).show()
    console.log("#editCommentDiv_"+edit_id)
    $("#editComment").val($("#"+edit_comment_id).val())

    function validateCommentForm(){
        var editeValue = $("#editedComment_"+edit_id).val()
        if (!editeValue || editeValue == ""){
            $("#Comment_help_"+edit_comment_id).text("You cannot leave the comment empty").addClass('text-danger')
            return false
        }
        else{
            $("#Comment_help_"+edit_comment_id).text("").removeClass('text-danger')
            return true
        }
    }
}

function  delete_comment(id){
    var delete_id = parseInt(id)
    var result = confirm("Are you sure you want to delete this comment?")
    if (result) {
        var data = {'id':delete_id}
        $.ajax({
            type: "POST",
            url: "/delete-comment/"+delete_id+'/',
            headers: {
                'X-CSRFToken': csrfToken 
            },
            data: data,
            success: function (response) {
                if (response.status == "success"){
                    alert("comment deleted successully")
                    setTimeout(() => {
                        window.location.reload()
                    }, 1000);
                }
            }
        });
    }
}

function getCSRFToken() {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Check if the cookie starts with 'csrftoken'
            if (cookie.startsWith('csrftoken=')) {
                // Extract the token value
                cookieValue = decodeURIComponent(cookie.substring('csrftoken='.length));
                break;
            }
        }
    }
    return cookieValue;
}
