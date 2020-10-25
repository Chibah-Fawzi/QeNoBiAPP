from django.contrib import admin
from django.urls import path, include

from QeNoBiApp.views import GroupView, LinkView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('QeNoBiApp.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
