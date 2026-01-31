from django.urls import path
from .views import (CourseCreateListView,StudentCreateView,EnrollmentCreateView,EnrollmentListView)

urlpatterns = [
    path('courses/', CourseCreateListView.as_view()),
    path('students/', StudentCreateView.as_view()),
    path('enrollments/', EnrollmentCreateView.as_view()),
    path('enrollments/list/', EnrollmentListView.as_view()),
]
