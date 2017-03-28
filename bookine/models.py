from django.db import models


# Create your models here.

class Book(models.Model):
    class Meta:
        db_table = 'book'
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    thumbnail = models.CharField(max_length=2083, null=True)
    description = models.TextField(null=True)
    author = models.CharField(max_length=255)


class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=254)
    sdt = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    manager = models.IntegerField(default=0)
    book = models.ManyToManyField(Book,through="Cart")

class Cart(models.Model):
    class Meta:
        db_table = 'cart'
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    count = models.IntegerField()
    no = models.CharField(max_length=100)
    is_payment = models.IntegerField(default=0)

class History(models.Model):
    no = models.CharField(max_length=100,primary_key=True)
    delivery = models.IntegerField(default=0)





