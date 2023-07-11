from Manager.models import Installment
from django.urls import path
from Installment_system.settings import MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static
from django.conf import settings 
from . import views

urlpatterns = [
    path('', views.home),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('customer_list/', views.customer_list, name='customer_list'),
    path('all_accounts/', views.all_accounts, name='all_accounts'),
    path('all_order_list/', views.all_order_list, name='all_order_list'),
    path('customer_profile/<str:pk_text>/', views.customer_profile, name='customer_profile'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)