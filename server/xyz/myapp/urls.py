from django.contrib import admin
from django.urls import path, include
from myapp import views as myapp_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', myapp_views.product_list, name='product_list'),
    path('product/<int:pk>/', myapp_views.product_detail, name='product_detail'),
    path('product/new/', myapp_views.product_new, name='product_new'),
    path('product/<int:pk>/edit/', myapp_views.product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', myapp_views.product_delete, name='product_delete'),
    path('', myapp_views.product_list, name='home'),  # Add this line
]
