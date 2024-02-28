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
    $("#editCommentDiv").dialog({
        autoOpen: false,
        modal: true,
        resizable: false,
        width: 700,
        title: 'Edit Comment',
        buttons: {
            "Close": function() {
                $('#editCommentForm').trigger('reset');
                $(this).dialog("close");
            }
        },
        open: function (event, ui) {
            $(".ui-dialog-titlebar-close").hide();
        }
    })
    $("#editCommentDiv").dialog("open")
    $("#editComment").val($("#"+edit_comment_id).val())
    $.ajax({
        type: "POST",
        url: "editComment/"+edit_id+"/",
        headers: {
            'X-CSRFToken': csrfToken 
        },
        data: "data",
        dataType: "dataType",
        success: function (response) {
            
        }
    });
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
