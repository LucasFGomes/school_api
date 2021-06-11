from rest_framework import viewsets
from school.models import Student, Course
from .serializer import StudentSerializer, CourseSerializer


class StudentsViewSet(viewsets.ModelViewSet):
    """Listing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """Listing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer