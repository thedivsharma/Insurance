from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_image, name="upload_image"),
    path("buffer/", views.buffer_page, name="buffer_page"),
    path("output/", views.show_output, name="show_output"),
]
