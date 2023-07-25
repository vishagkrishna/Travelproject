from .  import views
from django.urls import path

urlpatterns = [
    # path('',views.menu,name='menu'),
    path('',views.demo,name='demo'),
    # path('about/',views.about,name='about'),
    # path('contact/',views.contact,name='contact')

]