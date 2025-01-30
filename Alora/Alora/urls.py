"""
URL configuration for Alora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from aloraapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('resetpassword',views.password_reset_request,name='resetpassword'),
    path('verifyotp',views.verify_otp,name='verifyotp'),
    path('newpassword',views.set_new_password,name='newpassword'),

    path('',views.index),
    path('reg',views.user_registration,name='reg'),
    path('log',views.user_login,name='log'),
    path('logout',views.logout_view,name='logout'),


    path('user',views.userhome,name='user'),
    path('viewuser',views.profile,name='viewuser'),

    path('edit',views.edit,name='edit'),

    path('viewd',views.decoration_details,name='viewd'),
    path('addd',views.add_decoration,name='addd'),

    path('food',views.food,name='food'),
    path('ad_fud',views.add_food,name='ad_fud'),

    path('adminh',views.adminhome,name='adminh'),
    path('admviewuser',views.viewusers,name='admviewuser'),
    path('viewhall',views.viewhall,name='viewhall'),
    path('addhall',views.addhall,name='addhall'),
    
    path('book',views.booking,name='book'),
    path('userviewbooking',views.user_view_booking,name='userviewbooking'),
    path('adminviewbooking',views.admin_view_booking,name='adminviewbooking'),
    path('acceptrejectbooking/<int:id>',views.accept_reject_booking,name='acceptrejectbooking'),
    path('stripe_payments/<int:id>',views.stripe_payments,name='stripe_payments'),
    path('payment_statuss/<int:id>',views.payment_statuss,name='payment_statuss'),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
