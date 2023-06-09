from django.db import models

#create your model here
class User(models.Model):
    objects = models.Manager()
    id = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    birthday = models.DateField()

class Admin(models.Model):  # 管理员表
    objects = models.Manager()
    id = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)

class Goods(models.Model):  # 商品表
    objects = models.Manager()
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=100)  # 保存路径
    price = models.DecimalField(max_digits=7, decimal_places=2)
    sort = models.CharField(max_length=10)
    num = models.IntegerField()  # 库存数量

class ShoppingCart(models.Model):  # 购物车表
    objects = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE) #外键
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE) #外键
    price = models.DecimalField(max_digits=7, decimal_places=2)
    num = models.IntegerField()

class Order(models.Model):  # 订单表
    objects = models.Manager()
    orderId = models.CharField(
        max_length=30, primary_key=True)  # order + datetime的字符串
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)
    time = models.DateTimeField()

class OrderInfo(models.Model):  # 订单明细表
    objects = models.Manager()
    orderId = models.ForeignKey(Order, on_delete=models.CASCADE)
    goods = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    num = models.IntegerField()

#建立视图：order和user的视图，在查询订单详情的时候，可以显示更多的信息～？

class OrderView(models.Model):
    objects = models.Manager()
    user_id = models.CharField(max_length=20)
    orderId = models.CharField(max_length=30, primary_key=True)  # order + datetime的字符串
    goods = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    num = models.IntegerField()
    time = models.DateTimeField()
    totalPrice = models.DecimalField(max_digits=7, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'OrderView'
