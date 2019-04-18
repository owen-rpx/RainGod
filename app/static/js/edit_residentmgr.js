$(function () {
    // 绑定创建家庭成员Tab
    var table_ids = [];
    var idx = 0;
    $("#btn_crt_member_frm").click(function () {
        $(".layui-tab").show();
        var t = new Date().valueOf();
        ++idx;
        table_ids.push(t);
        $.ajax({
            url: "/admin/dynresidenttable/" + t,
            type: "GET",
            success: function (data) {
                layui.use(['element'], function () {
                    var element = layui.element;
                    element.tabAdd('member_tab', {
                        title: '成员' + idx,
                        content: data,
                        id: 'm_' + idx
                    });
                    // 手动点击新建Tab
                    element.tabChange('member_tab', 'm_' + idx);
                });
            }
        });
    });
    layui.use('element', function () {
        var element = layui.element;
        //一些事件监听
        element.on('tabDelete(member_tab)', function (data) {
            var title_count = $(".layui-tab-title").find('li').length;
            if (title_count == 0) {
                table_ids = [];
                idx = 0;
                tab_set = {};
                $(".layui-tab").hide();
            }
        });
    });
    // 提交表单
    $("#btn_save_resident").click(function () {
        console.log("提交表单");
    });


});