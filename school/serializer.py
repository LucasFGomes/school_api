from rest_framework import serializers
from school.models import Student, Course, Matriculation


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class MatriculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculation
        fields = '__all__'


class ListMatriculationsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source='course.description')
    period = serializers.SerializerMethodField()
    class Meta:
        model = Matriculation
        fields = ['course', 'period']

    def get_period(self, object):
        return object.get_period_display()


class ListMatriculationsStudentsSerializer(serializers.ModelSerializer):
    student = serializers.ReadOnlyField(source='student.name')
    class Meta:
        model = Matriculation
        fields = ['student']
