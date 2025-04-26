from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact me', views.contact_me, name='contact_me'),
    path('web',views.web,name='web'),
    path('back',views.back,name='back'),
    path('frame',views.frame,name='frame')
]
admin.site.site_header="Developer Nikhitha"
admin.site.site_title="welcome to NIKKI's dashboard"
admin.site.index_title="welcome to my portifolio"