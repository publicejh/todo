from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/doc/', get_swagger_view(title='Rest API Document')),
    path('api/v1/', include('api.urls'))
]
