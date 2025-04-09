from DeliveryAgent import views
from django.urls import path,include
app_name='DeliveryAgent'

urlpatterns = [
    path('myprofile/',views.myprofile,name='myprofile'),
    path('editprofile/',views.editprofile,name='editprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('dahomepage/',views.dahomepage,name='dahomepage'),
    path('vieworders/',views.vieworders,name='vieworders'),
    path('collectorder/<int:id>',views.collectorder,name='collectorder'),
    path('myorder/',views.myorder,name='myorder'),
    path('delivered/<int:id>',views.delivered,name='delivered'),
    path('logout/',views.logout,name='logout'),

]

