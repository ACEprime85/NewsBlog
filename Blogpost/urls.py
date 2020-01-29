from django.urls import path
from .views import post_list, postDetailView, post_by_tag, showvideo, contact_us
from . import views


app_name= 'Blogpost'
urlpatterns = [
      
      path(r'', views.post_list, name='post_list'),    
      path('<int:pk>/', postDetailView.as_view(), name='post_detail'),
      path(r'tag/', views.post_by_tag, name='post_by_tag'),
      path(r'Vidoes/', views.showvideo, name='showvideo'),
      path(r'contact/', views.contact_us, name='contact_us'),
      
]

 