"""config URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions 
from drf_yasg.views import get_schema_view 
from drf_yasg import openapi 


schema_view = get_schema_view(
    openapi.Info(
        title="Admos Hotel API",
        default_version="v1",
        description="An API for Admos Hotel & Suites. The website tells a story about Admos, shows theirs amenities and provides a section where consumer can book a stay in the hotel.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="croftltdng@gmail.com", phone_number='09136762133'),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/', include('hotel.urls')),

    # services
    path("api/services/", include('hotel.urls.service_urls')),

    # booking
    path("api/bookings/", include('hotel.urls.booking_urls')),

    # users
    path("api/users/", include('hotel.urls.user_urls')),

    # user authentication
    path("api-authentication/", include('rest_framework.urls')),
    path('user-authentication/', include('dj_rest_auth.urls')),
    path('user-auth/registration/', include('dj_rest_auth.registration.urls')),

    # api interface
    path('json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)