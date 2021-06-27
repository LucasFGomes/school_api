from rest_framework import viewsets, generics
from school.models import Student, Course, Matriculation
from .serializer import StudentSerializer, CourseSerializer, MatriculationSerializer, ListMatriculationsSerializer, ListMatriculationsStudentsSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentsViewSet(viewsets.ModelViewSet):
    """Listing all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CoursesViewSet(viewsets.ModelViewSet):
    """Listing all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculationsViewSet(viewsets.ModelViewSet):
    """Listing all matriculations"""
    queryset = Matriculation.objects.all()
    serializer_class = MatriculationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ListMatriculations(generics.ListAPIView):
    """Listing matriculations the student"""
    serializer_class = ListMatriculationsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Matriculation.objects.filter(student_id=self.kwargs['pk'])
    

class ListMatriculationsStudents(generics.ListAPIView):
    """Listing matriculations students"""
    serializer_class = ListMatriculationsStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Matriculation.objects.filter(course_id=self.kwargs['pk'])
    
