from django.shortcuts import render, redirect
from Guest.models import *
from Administrator.models import *


# Create your views here.
def userregistration(request):
    District=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=='POST':
        user_name=request.POST.get("txt_regname")
        user_email=request.POST.get("txt_regemail")
        user_contact=request.POST.get("txt_regcontact")
        user_address=request.POST.get("txt_regaddress")
        place_id=tbl_place.objects.get(id=request.POST.get("place"))
        user_photo=request.FILES.get('txt_regphoto')
        user_password=request.POST.get("txt_password")  
        tbl_user.objects.create(user_name=user_name,user_email=user_email,user_contact=user_contact,user_address=user_address,place=place_id,user_photo=user_photo,user_password=user_password,)
        return redirect('Guest:userregistration')
    else:
        return render(request,'Guest/UserRegistration.html',{'District':District,'place':place})


def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('did'))
    return render(request,'Guest/ajaxplace.html',{'place':place})


def login(request):
    if request.method=='POST':
        admincount=tbl_admin.objects.filter(admin_email=request.POST.get('txt_uname'),admin_password=request.POST.get('txt_apassword')).count()
        usercount=tbl_user.objects.filter(user_email=request.POST.get('txt_uname'),user_password=request.POST.get('txt_apassword')).count()
        sellercount=tbl_seller.objects.filter(seller_email=request.POST.get('txt_uname'),seller_password=request.POST.get('txt_apassword')).count()
        dacount=tbl_deliveryagent.objects.filter(deliveryagent_email=request.POST.get('txt_uname'),deliveryagent_password=request.POST.get('txt_apassword')).count()
        
        if admincount > 0:
            admin=tbl_admin.objects.get(admin_email=request.POST.get('txt_uname'),admin_password=request.POST.get('txt_apassword'))
            request.session['aid']=admin.id
            return redirect('Admin:homepage')
        elif usercount > 0:
            user=tbl_user.objects.get(user_email=request.POST.get('txt_uname'),user_password=request.POST.get('txt_apassword'))
            request.session['uid']=user.id
            return redirect('User:userhomepage')
        elif sellercount > 0:
            seller=tbl_seller.objects.get(seller_email=request.POST.get('txt_uname'),seller_password=request.POST.get('txt_apassword'))
            request.session['sid']=seller.id
            if seller.seller_status==0:
                return render(request,'Guest/Login.html',{'msg':'pending'})
            elif seller.seller_status==2:
                return render(request,'Guest/Login.html',{'msg':'rejected'})
            else:
                return redirect('Seller:sellerhomepage')
        elif dacount > 0:
            delivery=tbl_deliveryagent.objects.get(deliveryagent_email=request.POST.get('txt_uname'),deliveryagent_password=request.POST.get('txt_apassword'))
            request.session['did']=delivery.id
            request.session['place']=delivery.place.id
            if delivery.deliveryagent_status==0:
                return render(request,'Guest/Login.html',{'msg':'pending'})
            elif delivery.deliveryagent_status==2:
                return render(request,'Guest/Login.html',{'msg':'rejected'})
            else:
                return redirect('DeliveryAgent:dahomepage')
        else:
            return render(request,'Guest/Login.html',{'msg':'invalid'})
    else:
        return render(request,'Guest/Login.html')
        

            


def sellerreg(request):
    District=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=='POST':
        seller_name=request.POST.get("txt_regname")
        seller_email=request.POST.get("txt_regemail")
        seller_contact=request.POST.get("txt_regcontact")
        seller_address=request.POST.get("txt_regaddress")
        place_id=tbl_place.objects.get(id=request.POST.get("place"))
        seller_logo=request.FILES.get('txt_logo')
        seller_proof=request.FILES.get('txt_proof')
        seller_password=request.POST.get("txt_password")  
        tbl_seller.objects.create(seller_name=seller_name,seller_email=seller_email,seller_contact=seller_contact,seller_address=seller_address,place=place_id,seller_logo=seller_logo,seller_proof=seller_proof,seller_password=seller_password,)
        return redirect('Guest:sellerreg')
    else:
        return render(request,'Guest/Seller.html',{'District':District,'place':place})


def Deliveryagentreg(request):
    District=tbl_district.objects.all()
    place=tbl_place.objects.all()
    if request.method=='POST':
        deliveryagent_name=request.POST.get("txt_regname")
        deliveryagent_email=request.POST.get("txt_regemail")
        deliveryagent_contact=request.POST.get("txt_regcontact")
        deliveryagent_address=request.POST.get("txt_regaddress")
        place_id=tbl_place.objects.get(id=request.POST.get("place"))
        deliveryagent_photo=request.FILES.get('txt_photo')
        deliveryagent_proof=request.FILES.get('txt_proof')
        deliveryagent_password=request.POST.get("txt_password")  
        tbl_deliveryagent.objects.create(deliveryagent_name=deliveryagent_name,deliveryagent_email=deliveryagent_email,deliveryagent_contact=deliveryagent_contact,deliveryagent_address=deliveryagent_address,place=place_id,deliveryagent_photo=deliveryagent_photo,deliveryagent_proof=deliveryagent_proof,deliveryagent_password=deliveryagent_password,)
        return redirect('Guest:Deliveryagentreg')
    else:
        return render(request,'Guest/DeliveryAgent.html',{'District':District,'place':place})


def index(request):
    return render(request,"Guest/index.html")