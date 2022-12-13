"""shop URL Configuration

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
from django.urls import path, include

# Settings option 
from django.conf import settings
from django.conf.urls.static import static
# from shopapp.views import product_detail, product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shopapp/', include('shopapp.urls', namespace='shopapp')),

    # path('', product_list, name='product_list'),
    # path('<slug:slug>', product_list, name='product_list_by_category'),
    # path('<int:id>', product_detail, name='product_detail')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    