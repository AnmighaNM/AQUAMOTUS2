from django.db import models
from WebAdmin.models import *
from Guest.models import *
# Create your models here.
class fd_user(models.Model):
    fd_username = models.CharField(max_length=50)
    fd_email = models.EmailField(unique=True)
    fd_phone = models.CharField(unique=True, max_length=10)
    fd_password = models.CharField(max_length=20)
    fd_role = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class fd_category(models.Model):
    user_id = models.ForeignKey(tbl_canteen, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)

class fd_menu(models.Model):
    user_id = models.ForeignKey(tbl_canteen, on_delete=models.CASCADE)
    category_id = models.ForeignKey(fd_category, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='fd_images/')
    quantity = models.CharField(max_length=100)
    diff = models.CharField(max_length=40)

class fd_cart(models.Model):
    user_id = models.ForeignKey(fd_user, on_delete=models.CASCADE)
    menu_id = models.ForeignKey(fd_menu, on_delete=models.CASCADE)
    quantity = models.IntegerField()
