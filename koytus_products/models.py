from django.db import models

# Create your models here.

class CategoryProduct(models.Model):
    category_name = models.CharField(max_length=100)


    def __str__(self):
        return self.category_name


class Products(models.Model):
    pr_name = models.CharField(max_length=55)
    pr_cost = models.FloatField()
    pr_descr = models.TextField()
    pr_image = models.FileField(upload_to="product_image")
    pr_count = models.IntegerField(default=0)
    pr_category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.pr_name



class UserCart(models.Model):
    user_id = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    pr_count = models.IntegerField(default=0)
    creates_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.product}"


"""
Category
    category_name
Products
    pr_name
    pr_cost
    pr_descr
    pr_image
    pr_count
    pr_category

UserCart
    user_id
    product
    pr_count
    creates_at


"""


