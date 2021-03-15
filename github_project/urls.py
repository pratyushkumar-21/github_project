
from django.contrib import admin
from django.urls import path,include
from accounts.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('accounts/', include('django.contrib.auth.urls')),
]
