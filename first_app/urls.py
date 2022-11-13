from django.urls import path
from first_app import views

#relative urls
app_name = "first_app"

urlpatterns = [
    
    path('',views.index, name = "index" ),
    path('member_form/', views.member_form, name = "member_form"),
    
]
