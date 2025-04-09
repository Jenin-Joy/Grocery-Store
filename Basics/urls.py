from django.urls import path,include
from Basics import views
urlpatterns = [
    path('calculator/',views.calculator,name='calculator'),
    path('smallestlargest/',views.largesmall,name='smallestlargest'),
]

