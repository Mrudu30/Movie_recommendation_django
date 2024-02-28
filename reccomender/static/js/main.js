$(document).ready(function () {
    console.log("jquery loaded")
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
    // $('#'+edit_comment_id).
}