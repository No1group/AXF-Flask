from flask import Blueprint, render_template, redirect, url_for

from App.models.models import FoodType, Goods

marketbp = Blueprint("marketbp", __name__)


def init_marketbp(app):
    app.register_blueprint(blueprint=marketbp)


@marketbp.route('/market/')
def index():
    return '薛科的market页面'

@marketbp.route('/markets/')
def market(request):
    return redirect(url_for("marketbp.marketWithParams", kwargs={"typeid": "104749", "childcid": '0', "sortrule": "0"}))

@marketbp.route('/')
def marketWithParams(typeid, childcid, sortrule):
    foodtypes = FoodType.query.all()
    goodsList = Goods.query.filter(categoryid=typeid)

    if childcid != "0":
        goodsList = goodsList.filter(childcid=childcid)

    """
        sortrule 
            0 默认排序，综合排序
            1 销量降序
            2 销量升序
            3 价格降序
            4 价格升序
    """
    if sortrule == "1":
        goodsList = goodsList.order_by("productnum")
    elif sortrule == "2":
        goodsList = goodsList.order_by("-productnum")
    elif sortrule == "3":
        goodsList = goodsList.order_by("-price")
    elif sortrule == "4":
        goodsList = goodsList.order_by("price")

    foodtype = foodtypes.filter(typeid=typeid).first()

    # print(foodtype.childtypenames)
    childtypesTran = []
    # 全部分类: 0  # 进口水果:103534#国产水果:103533
    childtypes = foodtype.childtypenames.split("#")
    # ["全部分类:0","进口水果:103534","国产水果:103533"]
    for item in childtypes:
        itemchild = item.split(":")
        childtypesTran.append(itemchild)
    # [["全部分类","0"],["进口水果","103534“]...]

    data = {
        "title": "闪购",
        "foodtypes": foodtypes,
        "goodslist": goodsList,
        "childtypetran": childtypesTran,
        "typeid": typeid,
        "childcid": childcid,
    }
    return render_template('market.html',context =data)
        # render(request, 'app/market/market.html', context=data)

# def notPayList(request):
#     username = request.session.get("username")
#
#     data = getOrders(username,0)
#
#     return render(request,'app/market/order/order_list.html',context=data)


# def notReceiveList(request):
#
#     username = request.session.get("username")
#
#     data = getOrders(username,1)
#
#     return render(request,'app/market/order/order_list_not_receive.html',context=data)
