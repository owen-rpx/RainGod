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
                layui.use('element', function () {
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
        //basic
        var subdistrict_name = $('#subdistrict_name').val();
        var subdistrict_id = $('#subdistrict_id').val();
        var household_id = $('#household_id').val();
        var household_name = $('#household_name').val();
        var household_telephone = $('#household_telephone').val();
        var building_id = $('#building_id').val();
        var house_id = $('#house_id').val();
        var admin_unit_address = $('#admin_unit_address').val();
        var household_domicile_address = $('#household_domicile_address').val();
        var household_type = $('#household_type').val();
        var household_domicile_type = $('#household_domicile_type').val();
        var house_type = $('#house_type').val();
        //member
        var memebers = [];
        for (let index = 0; index < table_ids.length; index++) {
            var dynId = table_ids[index];
            var m = $("#dyn_" + dynId);
            var name = m.find("#name_" + dynId).val();
            var relation = m.find("#relation_" + dynId).val();
            var gender = m.find("#gender_" + dynId).val();
            var nation = m.find("#nation_" + dynId).val();
            var education = m.find("#education_" + dynId).val();
            var household_type = m.find("#household_type_" + dynId).val();
            var politics = m.find("#politics_" + dynId).val();
            var join_party_date = m.find("#join_party_date_" + dynId).val();
            var religion = m.find("#religion_" + dynId).val();
            var domicile_address = m.find("#domicile_address_" + dynId).val();
            var domicile_chkin_date = m.find("#domicile_chkin_date_" + dynId).val();
            var domicile_chkout_date = m.find("#domicile_chkout_date_" + dynId).val();
            var birth_date = m.find("#birth_date_" + dynId).val();
            var age = m.find("#age_" + dynId).val();
            var ID_numbers = m.find("#ID_numbers_" + dynId).val();
            var phone_number = m.find("#phone_number_" + dynId).val();
            var organization_position = m.find("#organization_position_" + dynId).val();
            var residence_status = m.find("#residence_status_" + dynId).val();
            var heath_status = m.find("#heath_status_" + dynId).val();
            var medical_insurance = m.find("#medical_insurance_" + dynId).val();
            var endowment_insurance = m.find("#endowment_insurance_" + dynId).val();
            var is_job_will = m.find("#is_job_will_" + dynId).val();
            var married_status = m.find("#married_status_" + dynId).val();
            var married_date = m.find("#married_date_" + dynId).val();
            var is_only_child = m.find("#is_only_child_" + dynId).val();
            var is_have_only_child_certificate = m.find("#is_have_only_child_certificate_" + dynId).val();
            var birth_control = m.find("#birth_control_" + dynId).val();
            var is_have_second_child_plan = m.find("#is_have_second_child_plan_" + dynId).val();
            var population_type = m.find("#population_type_" + dynId).val();
            var housing_type = m.find("#housing_type_" + dynId).val();
            var housing_area = m.find("#housing_area_" + dynId).val();
            var buy_house_date = m.find("#buy_house_date_" + dynId).val();
            var is_have_house_certificate = m.find("#is_have_house_certificate_" + dynId).val();
            var is_have_car = m.find("#is_have_car_" + dynId).val();
            var is_living_guarantee = m.find("#is_living_guarantee_" + dynId).val();
            var is_empty_nest = m.find("#is_empty_nest_" + dynId).val();
            var is_live_alone = m.find("#is_live_alone_" + dynId).val();
            var is_leave_nest = m.find("#is_leave_nest_" + dynId).val();
            var is_want_community_mgr = m.find("#is_want_community_mgr_" + dynId).val();
            var is_want_community_activity = m.find("#is_want_community_activity_" + dynId).val();
            var is_want_community_volunteer = m.find("#is_want_community_volunteer_" + dynId).val();
            var is_join_party = m.find("#is_join_party_" + dynId).val();
            var is_domestication_dog = m.find("#is_domestication_dog_" + dynId).val();
            var domicile_chkin_2_date = m.find("#domicile_chkin_2_date_" + dynId).val();
            var domicile_chkout_2_date = m.find("#domicile_chkout_2_date_" + dynId).val();
            var latest_register_date = m.find("#latest_register_date_" + dynId).val();
            var community_proposal = m.find("#community_proposal_" + dynId).val();
            var remark = m.find("#remark_" + dynId).val();

            var residentIns = {
                name: name,
                sex: gender,
                minzu: nation,
                wenhua: education,
                hukou_type: household_type,
                zhengzhi_mianmao: politics,
                join_party_dt: join_party_date,
                belief: religion,
                huji_addr: domicile_address,
                huji_in_dt: domicile_chkin_date,
                huji_out_dt: domicile_chkout_date,
                birthday: birth_date,
                shenfenzheng: ID_numbers,
                phone: phone_number,
                work_addr_title: organization_position,
                juzhu_zhuangtai: residence_status,
                yibao_qingkuang: medical_insurance,
                yanglao_baoxian: endowment_insurance,
                jiuye_yixiang: is_job_will,
                married_status: married_status,
                married_dt: married_date,
                dusheng_zinv: is_only_child,
                dusheng_zinv_id: is_have_only_child_certificate,
                dusheng_zinv_dt: '',
                jieyu_cuoshi: birth_control,
                plan_more_child: is_have_second_child_plan,
                renkou_type: population_type,
                has_car: is_have_car,
                is_dibao: is_living_guarantee,
                is_kongchao: is_empty_nest,
                is_duju: is_live_alone,
                is_lichao: is_leave_nest,
                join_community_management: is_want_community_mgr,
                join_community_activity: is_want_community_activity,
                join_comminity_volunteer: is_want_community_volunteer,
                join_party: is_join_party,
                has_dog: is_domestication_dog,
                ruzhu_dt: '',
                ruhu_dt: latest_register_date,
                suggestion: community_proposal,
                comment: remark,
                renyuan_type: household_type,
                renyuan_relationship: relation,
                hu_id: household_id
            };
            // for(var re in residentIns){
            //     if(re)
            // }
            memebers.push(residentIns);
        }
        console.log(memebers);

        $.ajax({
            method: 'POST',
            url: '/admin/insertresident',
            data: JSON.stringify(memebers),
            dataType: 'json',
            headers: {
                "Content-Type": "application/json;charset=utf-8"
            },
            contentType: 'application/json; charset=utf-8',
            success: function (data) {
                console.log(data);
                window.location.href='/admin/residentmgr'
            },
            error: function (err) {
                console.log(err);
            }
        });
        // $.post('/admin/insertresident', {'data':JSON.stringify(memebers)}, function (str) {
        //     console.log(str);
        // });
    });


});