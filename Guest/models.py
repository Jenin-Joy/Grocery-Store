from django.db import models
from Administrator.models import * 
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=30)
    user_email=models.CharField(max_length=30)
    user_contact=models.CharField(max_length=30)
    user_address=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    user_photo=models.FileField(upload_to="Assets/User/photo/")
    user_password=models.CharField(max_length=30)


class tbl_seller(models.Model):
    seller_name=models.CharField(max_length=30)
    seller_email=models.CharField(max_length=30)
    seller_contact=models.CharField(max_length=30)
    seller_address=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    seller_logo=models.FileField(upload_to="Assets/Seller/logo/")
    seller_proof=models.FileField(upload_to="Assets/Seller/proof/")
    seller_password=models.CharField(max_length=30)
    seller_status=models.IntegerField(default=0)


class tbl_deliveryagent(models.Model):
    deliveryagent_name=models.CharField(max_length=30)
    deliveryagent_email=models.CharField(max_length=30)
    deliveryagent_contact=models.CharField(max_length=30)
    deliveryagent_address=models.CharField(max_length=30)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    deliveryagent_photo=models.FileField(upload_to="Assets/DeliveryAgent/photo/")
    deliveryagent_proof=models.FileField(upload_to="Assets/DeliveryAgent/proof/")
    deliveryagent_password=models.CharField(max_length=30)
    deliveryagent_status=models.IntegerField(default=0)
