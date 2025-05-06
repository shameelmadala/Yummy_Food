from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name="admin_home"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('admin_user', views.admin_user, name="admin_user"),
    path('admin_post', views.admin_post, name="admin_post"),
    path('admin_subcategory', views.admin_category, name="admin_category"),
    path('admin_add_subcategory', views.admin_add_category, name="admin_add_category"),
    path('admin_remove_subcategory/<int:id>', views.admin_remove_subcategory, name="admin_remove_subcategory"),
    path('admin_donation_request',views.admin_donation_request,name='admin_donation_request')
]
