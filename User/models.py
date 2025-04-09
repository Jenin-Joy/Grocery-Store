from django.db import models
from Guest.models import * 
from Seller.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_status=models.IntegerField(default=0)
    complaint_reply=models.CharField(max_length=30)
    complaint_replydate=models.DateField(null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)

    


class tbl_booking(models.Model):

    booking_date = models.DateField(auto_now_add=True)
    booking_amount = models.CharField(max_length=30)
    booking_status = models.IntegerField(default=0)
    user = models.ForeignKey(tbl_user, on_delete=models.CASCADE)
   

class tbl_cart(models.Model):
    cart_qty = models.IntegerField(default=1)
    cart_status = models.IntegerField(default=0)
    product = models.ForeignKey(tbl_product, on_delete=models.CASCADE)
    booking = models.ForeignKey(tbl_booking, on_delete=models.CASCADE)
    deliveryagent = models.ForeignKey(tbl_deliveryagent, on_delete=models.CASCADE,null=True)


class tbl_feedback(models.Model):
    feedback_name=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    seller=models.ForeignKey(tbl_seller,on_delete=models.CASCADE,null=True)



class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_review=models.CharField(max_length=500)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True)




  
