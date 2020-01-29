"""NewsBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import include, path
from django.contrib import admin
from django.urls import path
from . import views
from .views import index
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

app_name= 'NewsBlog'
urlpatterns = [
    path(r'', views.index, name='index'),
    path('admin/', admin.site.urls),
    path(r'Blog/', include('Blogpost.urls'), name='Blogpost'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_title='NewsBlog Admin'
admin.site.site_header='NewsBlog Admin Portal'
admin.site.index_title='Welcome to NewsBlog Admin Portal'
