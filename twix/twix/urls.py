from django.contrib import admin
from django.urls import include, path

from factory1.views import product_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list),
    path('factory1/', include('factory1.urls', namespace='factory1')),
    path('factory2/', include('factory2.urls', namespace='factory2')),

]
