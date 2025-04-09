from Guest import views
from django.urls import path,include
app_name='Guest'

urlpatterns = [
    path('userregistration/',views.userregistration,name='userregistration'),
    path('ajaxplace/',views.ajaxplace,name='ajaxplace'),
    path('login/',views.login,name='login'),
    path('sellerreg/',views.sellerreg,name='sellerreg'),
    path('Deliveryagentreg/',views.Deliveryagentreg,name='Deliveryagentreg'),
    path('',views.index,name='index'),
    
]

