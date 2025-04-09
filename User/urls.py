from User import views
from django.urls import path,include
app_name='User'

urlpatterns = [
    path('userhomepage/',views.userhomepage,name='userhomepage'),
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('complaint/<int:id>',views.complaint,name='complaint'),
    path('viewseller/',views.viewseller,name='viewseller'), 
    path('viewdeliveryagent/<int:did>',views.viewdeliveryagent,name='viewdeliveryagent'), 
    path('viewproduct/<int:did>',views.viewproduct,name='viewproduct'), 
    path('Addcart/<int:pid>',views.Addcart,name='Addcart'), 
    path('Mycart/',views.Mycart, name='Mycart'),   
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),

    path("productpayment/", views.productpayment,name="productpayment"),
    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),

    path('feedback/',views.feedback,name='feedback'),
    path('mybooking/',views.mybooking,name='mybooking'),
    path('viewcartproduct/<int:id>',views.viewcartproduct,name='viewcartproduct'),
    path("viewcomplaint/", views.viewcomplaint,name="viewcomplaint"),
  
    path('rating/<int:mid>',views.rating,name="rating"),  
    path('ajaxstar/',views.ajaxstar,name="ajaxstar"),
    path('starrating/',views.starrating,name="starrating"),

    path('ajaxsubcategory/',views.ajaxsubcategory,name='ajaxsubcategory'),
    path('ajaxsearch/',views.ajaxsearch,name='ajaxsearch'),
     path('ajaxsellersearch/',views.ajaxsellersearch,name='ajaxsellersearch'),
    path('logout/',views.logout,name='logout'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    
    

]



