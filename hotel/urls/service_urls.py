from django.urls import path 
from hotel.views import service_views as views
from rest_framework.schemas import get_schema_view


urlpatterns = [
    path('rooms/', views.bookRooms, name='rooms'),
    path('rooms/<str:pk>/', views.bookRoom, name='room'),
    path('events/', views.bookEvents, name='events'),
    path('events/<str:pk>/', views.bookEvent, name='event'),

    path('openapi/', get_schema_view( 
    title="Admos Hotel & Suites",
    description="A website for Admos Hotel & Suites. The website tells a story about Admos, shows theirs amenities and provides a section where consumer can book a stay in the hotel.",
    version="1.0.0"
    ), name='admos_hotelapi-schema'),
]
