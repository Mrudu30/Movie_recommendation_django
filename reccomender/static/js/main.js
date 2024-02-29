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
    $("#editCommentDiv_"+edit_id).show()
    var oldComment = $("#comment_"+edit_id).text()
    // console.log("#comment_"+edit_id)
    // console.log(oldComment)
    $("#editComment_"+edit_id).val(oldComment)

    $("#editComment_"+edit_id).keyup(validateCommentForm)
    $("#editComment_"+edit_id).blur(validateCommentForm)

    function validateCommentForm(){
        var editeValue = $("#editComment_"+edit_id).val()
        console.log(editeValue)
        if (editeValue){
            $("#Comment_help_"+edit_id).text("").removeClass('text-danger')
            return true
            }
        else{
            $("#Comment_help_"+edit_id).text("You cannot leave the comment empty").addClass('text-danger')
            return false
        }
    }
    
    $("#editCommentForm_"+edit_id).submit(function(e){
        e.preventDefault()
        if (validateCommentForm()){
            $.ajax({
                type: "POST",
                url: "/editComment/"+edit_id+"/",
                headers: {
                    'X-CSRFToken': csrfToken 
                },
                data: {'id' : edit_id,'editedComment':$("#editComment_"+edit_id).val()},
                success: function (response) {
                    if(response.status=="success"){
                        alert("comment edited successfully");
                        setTimeout(() => {
                            window.location.reload()
                        }, 1000);
                    }
                    else{
                        alert("comment not edited");
                        window.location.reload() 
                    }
                }
            });
        }
    })
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
