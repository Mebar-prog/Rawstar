from django.contrib import admin
from django.urls import path,include
# from rest_framework import routers




urlpatterns = [
    path('jet/', include('jet.urls', 'jet')), 
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    # path('', include(router.urls)),



] 
