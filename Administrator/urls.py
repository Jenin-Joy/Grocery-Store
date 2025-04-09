from Administrator import views
from django.urls import path,include
app_name='Admin'

urlpatterns = [
    path('adminregistration/',views.adminregistration,name='adminregistration'),
    path('district/',views.district,name='district'),
    path('category/',views.category,name='category'),
    path('deletedistrict/<int:did>',views.deletedistrict,name='deletedistrict'),
    path('editdistrict/<int:did>',views.editdistrict,name='editdistrict'),
    path('deleteadmin/<int:did>',views.deleteadmin,name='deleteadmin'),
    path('editadmin/<int:did>',views.editadmin,name='editadmin'),
    path('deletecategory/<int:did>',views.deletecategory,name='deletecategory'),
    path('editcategory/<int:did>',views.editcategory,name='editcategory'),
    path('place/',views.place,name='place'),
    path('deleteplace/<int:did>',views.deleteplace,name='deleteplace'),
    path('editplace/<int:did>',views.editplace,name='editplace'),
    path('subcategory/',views.subcategory,name='subcategory'),
    path('deletesubcategory/<int:did>',views.deletesubcategory,name='deletesubcategory'),
    path('editsubcategory/<int:did>',views.editsubcategory,name='editsubcategory'),
    path('department/',views.department,name='department'),
    path('deletedepartment/<int:did>',views.deletedepartment,name='deletedepartment'),
    path('editdepartment/<int:did>',views.editdepartment,name='editdepartment'),
    path('designation/',views.designation,name='designation'),
    path('deletedesignation/<int:did>',views.deletedesignation,name='deletedesignation'),
    path('editdesignation/<int:did>',views.editdesignation,name='editdesignation'),
    path('employee/',views.employee,name='employee'),
    path('deleteemployee/<int:did>',views.deleteemployee,name='deleteemployee'),    
    path('editemployee/<int:did>',views.editemployee,name='editemployee'),
    path('homepage/',views.homepage,name='homepage'),
    
    path('sellerverification/',views.sellerverification,name='sellerverification'),
    path('deliveryagentverification/',views.deliveryagentverification,name='deliveryagentverification'),
    path('rejectseller/<int:did>',views.rejectseller,name='rejectseller'),  
    path('acceptseller/<int:did>',views.acceptseller,name='acceptseller'),   
    path('viewseller/',views.viewseller,name='viewseller'),
    path('rejectdeliveryagent/<int:did>',views.rejectdeliveryagent,name='rejectdeliveryagent'),  
    path('acceptdeliveryagent/<int:did>',views.acceptdeliveryagent,name='acceptdeliveryagent'),   
    path('viewdeliveryagent/',views.viewdeliveryagent,name='viewdeliveryagent'),
    path('viewuserfeedback/',views.viewuserfeedback,name='viewuserfeedback'),
    path('viewsellerfeedback/',views.viewsellerfeedback,name='viewsellerfeedback'),
    path('bookingreport/',views.bookingreport,name='bookingreport'),
    path('logout/',views.logout,name='logout'),
    
]



