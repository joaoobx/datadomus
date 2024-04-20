from django.contrib import admin
from django.urls import path, include

from example import views
from example.views import (
    ExampleListView,
    ExampleCreateView,
    ExampleUpdateView,
    ExampleDeleteView,
    ExampleCompleteView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('example/', include('example.urls')),
    path('', include('users.urls')),
    path('users/', include('django.contrib.auth.urls'))
]
