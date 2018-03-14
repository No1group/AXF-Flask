from sqlalchemy.ext.declarative import AbstractConcreteBase
from sqlalchemy.ext.declarative.base import declared_attr

from App.ext import models


class BaseMain(AbstractConcreteBase):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    name = models.Column(models.String(100))
    img = models.Column(models.String(200))
    trackid = models.Column(models.String(32))


class MainWheel(BaseMain, models.Model):
    __tablename__ = 'axf_wheel'



class MainNav(BaseMain, models.Model):
    __tablename__ = 'axf_nav'




class MainMustBuy(BaseMain, models.Model):
    __tablename__ = 'axf_mustbuy'



class MainShop(BaseMain, models.Model):
    __tablename__ = 'axf_shop'



"""
    trackid,name,img,categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,img2,childcid2,productid2,longname2,price2,marketprice2,img3,childcid3,productid3,longname3,price3,marketprice3
"""
class MainShow(BaseMain, models.Model):
    __tablename__ = 'axf_mainshow'
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    categoryid = models.Column(models.String(32))
    brandname = models.Column(models.String(100))
    img1 = models.Column(models.String(200))
    childcid1 = models.Column(models.String(32))
    productid1 = models.Column(models.String(32))
    longname1 = models.Column(models.String(200))
    price1 = models.Column(models.String(100))
    marketprice1 = models.Column(models.String(100))
    img2 = models.Column(models.String(200))
    childcid2 = models.Column(models.String(32))
    productid2 = models.Column(models.String(32))
    longname2 = models.Column(models.String(200))
    price2 = models.Column(models.String(100))
    marketprice2 = models.Column(models.String(100))
    img3 = models.Column(models.String(200))
    childcid3 = models.Column(models.String(32))
    productid3 = models.Column(models.String(32))
    longname3 = models.Column(models.String(200))
    price3 = models.Column(models.String(32))
    marketprice3 = models.Column(models.String(100))




"""
    typeid,typename,childtypenames,typesort
"""
class FoodType(models.Model):
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    __tablename__ = "axf_foodtypes"
    typeid = models.Column(models.String(32))
    typename = models.Column(models.String(100))
    childtypenames = models.Column(models.String(200))
    typesort = models.Column(models.String(32))



"""
    productid,productimg,productname,productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,childcid,childcidname,dealerid,storenums,productnum
"""
class Goods(models.Model):
    __tablename__ = "axf_goods"
    id = models.Column(models.Integer, primary_key=True, autoincrement=True)
    productid = models.Column(models.String(32))
    productimg = models.Column(models.String(200))
    productname = models.Column(models.String(100))
    productlongname = models.Column(models.String(200))
    isxf = models.Column(models.Boolean,default=False)
    pmdesc = models.Column(models.String(100))
    specifics = models.Column(models.String(100))
    price = models.Column(models.String(100))
    marketprice = models.Column(models.String(100))
    categoryid = models.Column(models.String(32))
    childcid = models.Column(models.String(32))
    childcidname = models.Column(models.String(100))
    dealerid = models.Column(models.String(32))
    storenums = models.Column(models.String(32))
    productnum = models.Column(models.String(32))









