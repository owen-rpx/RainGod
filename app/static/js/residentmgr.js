$(function() {

    // 绑定创建家庭成员表单
    var table_ids = [];
    $("#btn_crt_member_frm").click(function() {
        var t = new Date().valueOf();
        table_ids.push(t);
        $.ajax({
            url: "/admin/dynresidenttable/" + t,
            type: "GET",
            success: function(data) {
                $("#res_sets").append(data);
            }
        });
    });


});