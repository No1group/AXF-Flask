$(function () {
    $('#type_toggle').click(function () {
        $(this).find('#all_type_icon').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
        $('#sort_icon').addClass('glyphicon-menu-down').removeClass('glyphicon-menu-up')
        $('#type_container').show()
        $('#sort_container').hide()

    })

    $('#type_container').click(function () {
        $('#all_type_icon').addClass('glyphicon-menu-down').removeClass('glyphicon-menu-up')
        $(this).hide()
    })

    $('#sort_toggle').click(function () {
        $(this).find('#sort_icon').removeClass('glyphicon-menu-down').addClass('glyphicon-menu-up')
        $('#all_type_icon').addClass('glyphicon-menu-down').removeClass('glyphicon-menu-up')

        $('#sort_container').show()
        $('#type_container').hide()
    })
    $('#sort_container').click(function () {
        $('#sort_icon').addClass('glyphicon-menu-down').removeClass('glyphicon-menu-up')
        $(this).hide()

    })

    $(".addgoods").click(function () {
        //    添加商品到购物车   商品唯一标识  id
        //    prop 获取的设置的都是系统中自带的
        //    attr 可以获取任意属性，设置任意属性
        var goodsid = $(this).attr("goodsid");
        var goods = $(this);
        $.getJSON("/app/addtocart/", {"goodsid": goodsid}, function (data) {
            console.log(data);
            if (data["status"] == "302") {
                window.open("/app/login/", target = "_self");
            } else if (data["status"] == "200") {
                console.log(data["c_num"]);
                goods.prev("span").html(data["c_num"]);
            }
        })
    })
    $(".subgoods").click(function () {
        var subgoods = $(this);
        var goodsid = subgoods.parents("section").attr("goodsid");
        console.log(goodsid);
        var goods_num = subgoods.next("span");
        console.log(goods_num);
        if (goods_num.html() != 0) {
            $.getJSON("/app/subtocart/", {"goodsid": goodsid}, function (data) {
                console.log(data);
                if (data["status"] == "200"){
                    goods_num.html(data["num"]);
                }else if(data["status"] == "302"){
                    window.open("/app/login/",target="_self");
                }else if(data["status"] == "202"){
                    console.log("操作数据不存在");
                }
            })
        }else{
            console.log("操作无效");
        }
    })


})
    })

})