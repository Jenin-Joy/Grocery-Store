from django.shortcuts import render,redirect
from Administrator.models import *
from Guest.models import *
from User.models import *
from datetime import date
from django.conf import settings
from django.core.mail import send_mail



# Create your views here.
def logout(request):
    del request.session['aid']
    return redirect('Guest:login')

def adminregistration(request):
    if 'aid' not in request.session:
        return redirect('Guest:login')
    admin=tbl_admin.objects.all()
    if request.method=='POST':
        tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_contact=request.POST.get('txt_contact'),
        admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_password'))
        return redirect('Admin:adminregistration')
        
    else:
         return render(request,'Administrator/AdminRegistration.html',{'admin':admin})


def deleteadmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('Admin:adminregistration')

def editadmin(request,did):
    admi=tbl_admin.objects.get(id=did)
    if request.method=="POST":
        admi.admin_name=request.POST.get('txt_name')
        admi.admin_contact=request.POST.get('txt_contact')
        admi.admin_email=request.POST.get('txt_email')
        admi.admin_password=request.POST.get('txt_password')
        admi.save()
        return redirect('Admin:adminregistration')
    else:
        return render(request,'Administrator/AdminRegistration.html',{'editadmin':admi})




def district(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        tbl_district.objects.create(district_name=request.POST.get('txt_disname'),)
        return redirect('Admin:district')
        
    else:
         return render(request,'Administrator/District.html',{'district':district})


def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect('Admin:district')

def editdistrict(request,did):
    dist=tbl_district.objects.get(id=did)
    if request.method=="POST":
        dist.district_name=request.POST.get('txt_disname')
        dist.save()
        return redirect('Admin:district')
    else:
        return render(request,'Administrator/District.html',{'editdist':dist})



def category(request):
    category=tbl_category.objects.all()
    if request.method=='POST':
        tbl_category.objects.create(category_name=request.POST.get('txt_cname'),)
        return redirect('Admin:category')
        
    else:
         return render(request,'Administrator/Category.html',{'category':category})


def deletecategory(request,did):
    tbl_category.objects.get(id=did).delete()
    return redirect('Admin:category')


def editcategory(request,did):
    cat=tbl_category.objects.get(id=did)
    if request.method=="POST":
        cat.category_name=request.POST.get('txt_cname')
        cat.save()
        return redirect('Admin:category')
    else:
        return render(request,'Administrator/Category.html',{'editcat':cat})





def place(request):
        District=tbl_district.objects.all()
        placedata=tbl_place.objects.all()
        if request.method=='POST':
            place_name=request.POST.get("pname")
            place_pincode=request.POST.get("pincode")
            district_id=tbl_district.objects.get(id=request.POST.get("district"))
            tbl_place.objects.create(place_name=place_name,district=district_id,place_pincode=place_pincode)
            return redirect('Admin:place')
        else:
            return render(request,'Administrator/Place.html',{'District':District,'placedata':placedata})

def deleteplace(request,did):
    tbl_place.objects.get(id=did).delete()
    return redirect('Admin:place')

def editplace(request,did):
    District=tbl_district.objects.all()
    pla=tbl_place.objects.get(id=did)
    if request.method=="POST":
        pla.place_name=request.POST.get('pname')
        pla.place_pincode=request.POST.get('pincode')
        pla.district=tbl_district.objects.get(id=request.POST.get("district"))
        pla.save()
        return redirect('Admin:place')
    else:
        return render(request,'Administrator/Place.html',{'District':District,'editpla':pla})




def subcategory(request):
        category=tbl_category.objects.all()
        subcategorydata=tbl_subcategory.objects.all()
        if request.method=='POST':
            subcategory_name=request.POST.get("scname")
            category_id=tbl_category.objects.get(id=request.POST.get("category"))
            tbl_subcategory.objects.create(subcategory_name=subcategory_name,category=category_id,)
            return redirect('Admin:subcategory')
        else:
            return render(request,'Administrator/Subcategory.html',{'category':category,'subcategorydata':subcategorydata})

def deletesubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()
    return redirect('Admin:subcategory')

def editsubcategory(request,did):
    category=tbl_category.objects.all()
    sub=tbl_subcategory.objects.get(id=did)
    if request.method=="POST":
        sub.subcategory_name=request.POST.get('scname')
        sub.category=tbl_category.objects.get(id=request.POST.get("category"))
        sub.save()
        return redirect('Admin:subcategory')
    else:
        return render(request,'Administrator/Subcategory.html',{'category':category,'editsub':sub})
        


def department(request):
    department=tbl_department.objects.all()
    if request.method=='POST':
        tbl_department.objects.create(department_name=request.POST.get('txt_depname'),)
        return redirect('Admin:department')
        
    else:
         return render(request,'Administrator/Department.html',{'department':department})


def deletedepartment(request,did):
    tbl_department.objects.get(id=did).delete()
    return redirect('Admin:department')


def editdepartment(request,did):
    dep=tbl_department.objects.get(id=did)
    if request.method=="POST":
        dep.department_name=request.POST.get('txt_depname')
        dep.save()
        return redirect('Admin:department')
    else:
        return render(request,'Administrator/Department.html',{'editdep':dep})





def designation(request):
    designation=tbl_designation.objects.all()
    if request.method=='POST':
        tbl_designation.objects.create(designation_name=request.POST.get('txt_desname'),)
        return redirect('Admin:designation')
        
    else:
         return render(request,'Administrator/Designation.html',{'designation':designation})


def deletedesignation(request,did):
    tbl_designation.objects.get(id=did).delete()
    return redirect('Admin:designation')


def editdesignation(request,did):
    des=tbl_designation.objects.get(id=did)
    if request.method=="POST":
        des.designation_name=request.POST.get('txt_desname')
        des.save()
        return redirect('Admin:designation')
    else:
        return render(request,'Administrator/Designation.html',{'editdes':des})

def employee(request):
        Department=tbl_department.objects.all()
        Designation=tbl_designation.objects.all()
        employeedata=tbl_employee.objects.all()
        if request.method=='POST':
            employee_name=request.POST.get("txt_empname")
            employee_contact=request.POST.get("txt_empcontact")
            employee_email=request.POST.get("txt_empemail")
            employee_address=request.POST.get("txt_empaddress")
            employee_basicsalary=request.POST.get("txt_empbs")
            department_id=tbl_department.objects.get(id=request.POST.get("department"))
            designation_id=tbl_designation.objects.get(id=request.POST.get("designation"))
            tbl_employee.objects.create(employee_name=employee_name,employee_contact=employee_contact,employee_email=employee_email,employee_address=employee_address,employee_basicsalary=employee_basicsalary,department=department_id,designation=designation_id)
            return redirect('Admin:employee')
        else:
            return render(request,'Administrator/Employee.html',{'Department':Department,'Designation':Designation,'employeedata':employeedata})

def deleteemployee(request,did):
    tbl_employee.objects.get(id=did).delete()
    return redirect('Admin:employee')

def editemployee(request,did):
    Department=tbl_department.objects.all()
    Designation=tbl_designation.objects.all()
    emp=tbl_employee.objects.get(id=did)
    if request.method=="POST":
        emp.employee_name=request.POST.get('txt_empname')
        emp.employee_contact=request.POST.get("txt_empcontact")
        emp.employee_email=request.POST.get("txt_empemail")
        emp.employee_address=request.POST.get("txt_empaddress")
        emp.employee_basicsalary=request.POST.get("txt_empbs")
        emp.department=tbl_department.objects.get(id=request.POST.get("department"))
        emp.designation=tbl_designation.objects.get(id=request.POST.get("designation"))
        emp.save()
        return redirect('Admin:employee')
    else:
        return render(request,'Administrator/Employee.html',{'Department':Department,'Designation':Designation,'editemp':emp})
        
def homepage(request):
    return render(request,'Administrator/Home.html')




    
def sellerverification(request):
    seller=tbl_seller.objects.filter(seller_status=0)
    return render(request,'Administrator/Sellerverification.html',{'seller':seller})

def deliveryagentverification(request):
    delivery=tbl_deliveryagent.objects.filter(deliveryagent_status=0)
    return render(request,'Administrator/Deliveryagentverification.html',{'delivery':delivery})

def acceptseller(request,did):
    seller=tbl_seller.objects.get(id=did)
    seller.seller_status=1
    seller.save()
    subject = "Seller  Verification Successful"
    body = (f"Respected {seller.seller_name},\n\n"
            f"Your account '{seller.seller_name}' has been successfully verified.\n\n"
            f"Registered Details:\n"
           
            f"Address: {seller.seller_address}\n"
            f"Contact: {seller.seller_contact}\n\n"
            "You can now start using our platform.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [seller.seller_email],
        fail_silently=False,
    )
    return redirect('Admin:viewseller')


def rejectseller(request,did):
    seller=tbl_seller.objects.get(id=did)
    seller.seller_status=2
    seller.save()
    subject = "Seller Verification Failed"
    body = (f"Respected {seller.seller_name},\n\n"
            f"Sorry,Your account '{seller.seller_name}' has been rejected.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [seller.seller_email],
        fail_silently=False,
    )
    return redirect('Admin:viewseller')


def viewseller(request):
    aseller=tbl_seller.objects.filter(seller_status=1)
    rseller=tbl_seller.objects.filter(seller_status=2)
    if request.method=="POST":
        return redirect('Admin:viewseller')
    else:
         return render(request,'Administrator/viewseller.html',{'aseller':aseller,'rseller':rseller})


def acceptdeliveryagent(request,did):
    deliveryagent=tbl_deliveryagent.objects.get(id=did)
    deliveryagent.deliveryagent_status=1
    deliveryagent.save()
    subject = "Delivery Agent Verification Successful"
    body = (f"Respected {deliveryagent.deliveryagent_name},\n\n"
            f"Your account '{deliveryagent.deliveryagent_name}' has been successfully verified.\n\n"
            f"Registered Details:\n"
           
            f"Address: {deliveryagent.deliveryagent_address}\n"
            f"Contact: {deliveryagent.deliveryagent_contact}\n\n"
            "You can now start using our platform.\n\n"
            "Best Regards,\n Team")
    
    send_mail(
        subject,
        body,
        settings.EMAIL_HOST_USER,
        [deliveryagent.deliveryagent_email],
        fail_silently=False,
    )
    return redirect('Admin:viewdeliveryagent')


def rejectdeliveryagent(request,did):
    rda=tbl_deliveryagent.objects.get(id=did)
    rda.deliveryagent_status=2
    rda.save()
    return redirect('Admin:viewdeliveryagent')

def viewdeliveryagent(request):
    adelivery=tbl_deliveryagent.objects.filter(deliveryagent_status=1)
    rdelivery=tbl_deliveryagent.objects.filter(deliveryagent_status=2)
    if request.method=="POST":
        return redirect('Admin:viewdeliveryagent')
    else:
         return render(request,'Administrator/viewdeliveryagent.html',{'adelivery':adelivery,'rdelivery':rdelivery})

def viewuserfeedback(request):
    user=tbl_user.objects.all()
    feedback=tbl_feedback.objects.filter(user__in=user)
    return render(request,'Administrator/viewfeedback.html',{'feedback':feedback})

def viewsellerfeedback(request):
    seller=tbl_seller.objects.all()
    feedback=tbl_feedback.objects.filter(seller__in=seller)
    return render(request,'Administrator/viewsellerfeedback.html',{'feedback':feedback})

def bookingreport(request):
    if "aid" not in request.session:
        return redirect('Guest:login')
    if  request.method == "POST":
        cart=tbl_cart.objects.filter(booking__booking_date__gt=request.POST.get("txt_fromdate"),booking__booking_date__lt=request.POST.get("txt_todate"))
        return render(request,'Administrator/BookingReport.html',{'cart':cart})
    else:    
        return render(request,'Administrator/BookingReport.html')


