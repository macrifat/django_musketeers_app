from django.urls import path
from first_app import views

#relative urls
app_name = "first_app"

urlpatterns = [
    
    path('',views.index, name = "index" ),
    path('member_form/', views.member_form, name = "member_form"),
    path('member_info/<int:member_id>/', views.member_info, name = "member_info"),
    path('member_update/<int:member_id>/', views.member_update, name = "member_update"),
    path('member_delete/<int:member_id>/', views.member_delete, name = "member_delete"),
    
]
