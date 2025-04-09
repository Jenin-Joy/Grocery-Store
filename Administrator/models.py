from django.db import models

# Create your models here.
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=20)
    admin_contact=models.CharField(max_length=20)
    admin_email=models.CharField(max_length=20)
    admin_password=models.CharField(max_length=20)
    
class tbl_district(models.Model):
    district_name=models.CharField(max_length=20)


class tbl_category(models.Model):
    category_name=models.CharField(max_length=20)
    
class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    place_pincode=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=20)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)


class tbl_department(models.Model):
    department_name=models.CharField(max_length=20)

class tbl_designation(models.Model):
    designation_name=models.CharField(max_length=20)
    

class tbl_employee(models.Model):
    employee_name=models.CharField(max_length=30)
    employee_contact=models.CharField(max_length=30)
    employee_email=models.CharField(max_length=30)
    employee_address=models.CharField(max_length=30)
    employee_basicsalary=models.CharField(max_length=30)
    department=models.ForeignKey(tbl_department,on_delete=models.CASCADE)
    designation=models.ForeignKey(tbl_designation,on_delete=models.CASCADE)