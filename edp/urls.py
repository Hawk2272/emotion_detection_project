from django.urls import path
from edp.views import views

urlpatterns = [
    path('camera_input/', views.camera_input, name='camera_input'),
]