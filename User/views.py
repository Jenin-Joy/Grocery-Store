from django.shortcuts import render, redirect
from Guest.models import *
from Administrator.models import *
from User.models import *
from Seller.models import *
from django.db.models import Sum
# Create your views here.

def logout(request):
    del request.session['uid']
    return redirect('Guest:login') 

def userhomepage(request):
    return render(request,'User/Homepage.html')

def myprofile(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    return render(request,'User/MyProfile.html',{'user':user})

def editprofile(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    if request.method=="POST":
        user.user_name=request.POST.get('txt_name')
        user.user_email=request.POST.get('txt_email')
        user.user_contact=request.POST.get('txt_contact')
        user.user_address=request.POST.get('txt_address')
        user.save()
        return redirect('User:myprofile')
    else:
        return render(request,'User/EditProfile.html',{'user':user})

def changepassword(request):
    user=tbl_user.objects.get(id=request.session["uid"])
    dbpass=user.user_password
    if request.method=="POST":
        oldpassword=request.POST.get('txt_oldpass')
        newpassword=request.POST.get('txt_newpass')
        confirmpassword=request.POST.get('txt_conpass')
        if oldpassword==dbpass:
            if newpassword==confirmpassword:
                user.user_password=newpassword
                user.save()
                return redirect("User:myprofile")
    else:
        return render(request,'User/ChangePassword.html',{'user':user})
        

def complaint(request,id):
    userid=tbl_user.objects.get(id=request.session["uid"])
    complaint=tbl_complaint.objects.filter(user=userid)
    productid=tbl_product.objects.get(id=id)
    if request.method=='POST':
        complaint_title=request.POST.get("txt_subname")
        complaint_content=request.POST.get("txt_complaint")
        tbl_complaint.objects.create(complaint_title=complaint_title,complaint_content=complaint_content,user=userid,product=productid)
        return redirect('User:viewcomplaint')
    else:
        return render(request,'User/Postcomplaint.html')

def viewcomplaint(request):
    userid=tbl_user.objects.get(id=request.session["uid"])
    complaint=tbl_complaint.objects.filter(user=userid)
    return render(request,'User/ViewComplaint.html',{'complaint':complaint})




def viewdeliveryagent(request,did):
    delivery=tbl_deliveryagent.objects.get(id=did)
    return render(request,'User/viewdeliveryagent.html',{'delivery':delivery})




def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/Homepage.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/Homepage.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/Homepage.html",{'msg':msg})



def Mycart(request):
    if request.method=="POST":
        bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
        bookingdata.booking_amount=request.POST.get("carttotalamt")
        bookingdata.booking_status=1
        bookingdata.save()
        cart = tbl_cart.objects.filter(booking=bookingdata)
        for i in cart:
            i.cart_status = 1
            i.save()
        return redirect("User:productpayment")
    else:
        bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
        if bookcount > 0:
            book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
            request.session["bookingid"] = book.id
            cart = tbl_cart.objects.filter(booking=book)
            for i in cart:
                total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_count'))['total']
                total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
                # print(total_stock)
                # print(total_cart)
                if total_stock is None:
                    total_stock = 0
                if total_cart is None:
                    total_cart = 0
                total =  total_stock - total_cart
                i.total_stock = total
            return render(request,"User/MyCart.html",{'cartdata':cart})
        else:
            return render(request,"User/MyCart.html")

        

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")

def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:Mycart")   

def productpayment(request):
    bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
    amt = bookingdata.booking_amount
    cartdata=tbl_cart.objects.filter(booking=request.session['bookingid'])
    if request.method == "POST":
        bookingdata.booking_status = 2
        bookingdata.save()
        for i in cartdata:
            i.cart_status=2
            i.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amt})



def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")

def feedback(request):
    userid=tbl_user.objects.get(id=request.session["uid"])
    feedback=tbl_feedback.objects.filter(user=userid)
    if request.method=='POST':
        feedback_name=request.POST.get("txt_content")
        tbl_feedback.objects.create(feedback_name=feedback_name,user=userid,)
        return redirect('User:feedback')
    else:
        return render(request,'User/Feedback.html',{'feedback':feedback})


def mybooking(request): 
    booking=tbl_booking.objects.filter(booking_status=2,user=request.session["uid"])
    return render(request,'User/MyBooking.html',{'booking':booking})
    
def viewcartproduct(request,id): 
    cart=tbl_cart.objects.filter(booking=id)
    return render(request,'User/Viewcartproducts.html',{'cart':cart})

def rating(request,mid):
    parray=[1,2,3,4,5]
    mid=mid
    # wdata=tbl_booking.objects.get(id=mid)
    
    counts=0
    counts=stardata=tbl_rating.objects.filter(product=mid).count()
    if counts>0:
        res=0
        stardata=tbl_rating.objects.filter(product=mid).order_by('-datetime')
        for i in stardata:
            res=res+i.rating_data
        avg=res//counts
        # print(avg)
        return render(request,"User/Rating.html",{'mid':mid,'data':stardata,'ar':parray,'avg':avg,'count':counts})
    else:
         return render(request,"User/Rating.html",{'mid':mid})

def ajaxstar(request):
    parray=[1,2,3,4,5]
    rating_data=request.GET.get('rating_data')
    user_name=request.GET.get('user_name')
    user_review=request.GET.get('user_review')
    pid=request.GET.get('pid')
    # wdata=tbl_booking.objects.get(id=pid)
    tbl_rating.objects.create(user=tbl_user.objects.get(id=request.session["uid"]),user_review=user_review,rating_data=rating_data,product=tbl_product.objects.get(id=pid))
    stardata=tbl_rating.objects.filter(product=pid).order_by('-datetime')
    return render(request,"User/AjaxRating.html",{'data':stardata,'ar':parray})

def starrating(request):
    r_len = 0
    five = four = three = two = one = 0
    # cdata = tbl_booking.objects.get(id=request.GET.get("pdt"))
    rate = tbl_rating.objects.filter(product=request.GET.get("pdt"))
    ratecount = tbl_rating.objects.filter(product=request.GET.get("pdt")).count()
    for i in rate:
        if int(i.rating_data) == 5:
            five = five + 1
        elif int(i.rating_data) == 4:
            four = four + 1
        elif int(i.rating_data) == 3:
            three = three + 1
        elif int(i.rating_data) == 2:
            two = two + 1
        elif int(i.rating_data) == 1:
            one = one + 1
        else:
            five = four = three = two = one = 0
        # print(i.rating_data)
        # r_len = r_len + int(i.rating_data)
    # rlen = r_len // 5
    # print(rlen)
    result = {"five":five,"four":four,"three":three,"two":two,"one":one,"total_review":ratecount}
    return JsonResponse(result)



def ajaxsubcategory(request):
    subcategory=tbl_subcategory.objects.filter(category=request.GET.get('did'))
    return render(request,'User/ajaxsubcategory.html',{'subcategory':subcategory})


def ajaxplace(request):
    place=tbl_place.objects.filter(district=request.GET.get('pid'))
    return render(request,'User/ajaxplace.html',{'place':place})


def viewproduct(request,did):
    ar=[1,2,3,4,5]
    parry=[]
    avg=0
    category=tbl_category.objects.all()
    subcategory=tbl_subcategory.objects.all()
    district=tbl_district.objects.all()
    product = tbl_product.objects.filter(seller_id=did)
    for i in product:
        total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
        total_cart = tbl_cart.objects.filter(product=i.id, cart_status__gt=1).aggregate(total=Sum('cart_qty'))['total']
        # print(total_stock)
        # print(total_cart)
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total =  total_stock - total_cart
        i.total_stock = total


        tot=0
        ratecount=tbl_rating.objects.filter(product=i.id).count()
        if ratecount>0:
            ratedata=tbl_rating.objects.filter(product=i.id)
            for j in ratedata:
                tot=tot+j.rating_data
                avg=tot//ratecount
                #print(avg)
            parry.append(avg)
        else:
            parry.append(0)
        # print(parry)
    datas=zip(product,parry)
    return render(request,'User/viewproduct.html',{'product':datas,"ar":ar,'category':category,'subcategory':subcategory,'district':district,"seller_id":did})



def ajaxsearch(request):
    
    if (request.GET.get("cid")) and (request.GET.get("sid")):
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        product=tbl_product.objects.filter(subcategory=request.GET.get("sid"),seller=request.GET.get("seller_id"))

        for i in product:
            total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
            total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
            # print(total_stock)
            # print(total_cart)
            if total_stock is None:
                total_stock = 0
            if total_cart is None:
                total_cart = 0
            total =  total_stock - total_cart
            i.total_stock = total


            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(product,parry)
        return render(request,'User/ajaxsearch.html',{'product':datas,'ar':ar})
    elif (request.GET.get("cid")):
        ar=[1,2,3,4,5]
        parry=[]
        avg=0
        product=tbl_product.objects.filter(subcategory__category=request.GET.get("cid"),seller=request.GET.get("seller_id"))

        for i in product:
            total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_count'))['total']
            total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
            # print(total_stock)
            # print(total_cart)
            if total_stock is None:
                total_stock = 0
            if total_cart is None:
                total_cart = 0
            total =  total_stock - total_cart
            i.total_stock = total


            tot=0
            ratecount=tbl_rating.objects.filter(product=i.id).count()
            if ratecount>0:
                ratedata=tbl_rating.objects.filter(product=i.id)
                for j in ratedata:
                    tot=tot+j.rating_data
                    avg=tot//ratecount
                    #print(avg)
                parry.append(avg)
            else:
                parry.append(0)
            # print(parry)
        datas=zip(product,parry)
        return render(request,'User/ajaxsearch.html',{'product':datas,'ar':ar})
    else:
        return render(request,'User/ajaxsearch.html',{'msg':"No Product Found"})




def viewseller(request):
    district = tbl_district.objects.all()
    seller = tbl_seller.objects.all()
    return render(request, 'User/viewseller.html', {'seller': seller, 'district': district})

def ajaxsellersearch(request):
    district_id = request.GET.get("district")
    place_id = request.GET.get("place")

    if district_id and place_id:
        seller = tbl_seller.objects.filter(place__id=place_id, place__district__id=district_id)
    elif district_id:
        seller = tbl_seller.objects.filter(place__district__id=district_id)
    else:
        seller = tbl_seller.objects.all()

    return render(request, "User/ajaxsellersearch.html", {"seller": seller})