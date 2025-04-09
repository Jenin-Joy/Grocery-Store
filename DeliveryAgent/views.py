from django.shortcuts import render, redirect
from Guest.models import *
from Administrator.models import *
from User.models import *
from Seller.models import *
# Create your views here.

def logout(request):
    del request.session['did']
    return redirect('Guest:login')




def myprofile(request):
    delivery=tbl_deliveryagent.objects.get(id=request.session["did"])
    return render(request,'DeliveryAgent/MyProfile.html',{'delivery':delivery})


def editprofile(request):
    delivery=tbl_deliveryagent.objects.get(id=request.session["did"])
    if request.method=="POST":
        delivery.deliveryagent_name=request.POST.get('txt_name')
        delivery.deliveryagent_email=request.POST.get('txt_email')
        delivery.deliveryagent_contact=request.POST.get('txt_contact')
        delivery.deliveryagent_address=request.POST.get('txt_address')
        delivery.save()
        return redirect('DeliveryAgent:myprofile')
    else:
        return render(request,'DeliveryAgent/EditProfile.html',{'delivery':delivery})
    

def changepassword(request):
    delivery=tbl_deliveryagent.objects.get(id=request.session["did"])
    dbpass=delivery.deliveryagent_password
    if request.method=="POST":
        oldpassword=request.POST.get('txt_oldpass')
        newpassword=request.POST.get('txt_newpass')
        confirmpassword=request.POST.get('txt_conpass')
        if oldpassword==dbpass:
            if newpassword==confirmpassword:
                delivery.deliveryagent_password=newpassword
                delivery.save()
                return redirect("DeliveryAgent:myprofile")
    else:
        return render(request,'DeliveryAgent/ChangePassword.html',{'delivery':delivery})
   

def dahomepage(request):
    if 'did' not in request.session:
        return redirect('Guest:login')
    return render(request,'DeliveryAgent/homepage.html')


def vieworders(request): 
    cart=tbl_cart.objects.filter(cart_status=3,product__seller__place=request.session['place'])
    return render(request,'DeliveryAgent/vieworders.html',{'cart':cart})



def collectorder(request,id): 
    cartdata=tbl_cart.objects.get(id=id)
    cartdata.cart_status=4
    cartdata.deliveryagent=tbl_deliveryagent.objects.get(id=request.session['did'])
    cartdata.save()

    return redirect('DeliveryAgent:vieworders')


def myorder(request):
    cart = tbl_cart.objects.filter(cart_status__gte=4,deliveryagent=request.session['did'])
    return render(request, 'DeliveryAgent/Myorders.html', {'cart': cart})


def delivered(request,id): 
    collectorder=tbl_cart.objects.get(id=id)
    collectorder.cart_status=5
    collectorder.save()
    return redirect('DeliveryAgent:myorder')