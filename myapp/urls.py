
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('error/', views.error, name='error'),
    path('details/', views.details, name='details'),
    path('blog/', views.blog, name='blog'),
    path('', views.index, name='index'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),

]
