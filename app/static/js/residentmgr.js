$(function () {
    // 解决option文本过长问题
    $("select").on('change', function (evt) {
        var tar = evt.target;
        var checkText = $(tar).find("option:selected").text();
        $(tar).attr("title", checkText);
    });

    // 绑定并实例layui日期控件
    layui.use('laydate', function () {
        var laydate = layui.laydate;
        laydate.render({
            elem: '#join_party_date',
            zIndex: 99999999,
            trigger: 'click'
        });

        laydate.render({
            elem: '#domicile_chkin_date',
            zIndex: 99999999,
            trigger: 'click'
        });

        laydate.render({
            elem: '#domicile_chkout_date',
            zIndex: 99999999,
            trigger: 'click'
        });

        laydate.render({
            elem: '#birth_date',
            zIndex: 99999999,
            trigger: 'click'
        });

        laydate.render({
            elem: '#married_date',
            zIndex: 99999999,
            trigger: 'click'
        });

        laydate.render({
            elem: '#buy_house_date',
            zIndex: 99999999,
            trigger: 'click'
        });
        laydate.render({
            elem: '#domicile_chkin_2_date',
            zIndex: 99999999,
            trigger: 'click'
        });
        laydate.render({
            elem: '#domicile_chkout_2_date',
            zIndex: 99999999,
            trigger: 'click'
        });
        laydate.render({
            elem: '#latest_register_date',
            zIndex: 99999999,
            trigger: 'click'
        });


    });


});