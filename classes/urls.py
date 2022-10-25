from django.urls import path
from .import views
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path ('course/',views.Course_list),
    path ('coursedetail/<int:id>', views.Course_detail),
]

urlpatterns = format_suffix_patterns (urlpatterns)
