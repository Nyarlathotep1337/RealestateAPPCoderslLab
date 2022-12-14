"""RealestateAPPCoderslLab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from realestate_core import views

# from realestate_core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='index'),
    path('create_user/', views.CreateUserView.as_view(), name='create_user'),

    path('create_realtor/', views.CreateRealtorView.as_view(), name='create_realtor'),
    path('edit_realtor/<int:id>/', views.EditRealtorView.as_view(), name='edit_realtor'),
    path('delete_realtor/<int:id>/', views.DeleteRealtorView.as_view(), name='delete_realtor'),

    path('create_realestate/', views.CreateRealestateView.as_view(), name='create_realestate'),
    path('edit_realestate/<int:id>/', views.EditRealestateView.as_view(), name='edit_realestate'),
    path('delete_realestate/<int:id>/', views.DeleteRealestateView.as_view(), name='delete_realestate'),

    path('all_realtors/', views.RealtorListView.as_view(), name='realtor_list'),
    path('all_realestates/', views.AllRealestatesView.as_view(), name='realestate_list'),

    path('sell_buy/', views.SellBuyView.as_view(), name='Sell_Buy'),
    path('contact/', views.ContactView.as_view(), name='contact'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
