from rest_framework import serializers
from .models import Institute, Faculty, FacultyRoute, ModelLogo


class ModelLogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelLogo
        fields = ["id", "logo"]

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculty
        fields = ['id', 'facultetyName']


class FacultyRouteSerializer(serializers.ModelSerializer):
    faculty = FacultySerializer()

    class Meta:
        model = FacultyRoute
        fields = [
            'id', 'faculty', 'institute', 'routeCode', 'routeName',
            'routeType', 'daySum', 'nightSum', 'sirtqiSum',
            'dayKvota', 'nightKvota', 'sirtqiKvota', 'language'
        ]


class InstituteSerializer(serializers.ModelSerializer):
    faculty_routes = serializers.SerializerMethodField()

    class Meta:
        model = Institute
        fields = [
            'id', 'name', 'description', 'website', 'video',
            'photo', 'address', 'faculty_routes', 'grand', 'contract'
        ]

    def get_faculty_routes(self, obj):
        routes = FacultyRoute.objects.filter(institute=obj)
        return FacultyRouteSerializer(routes, many=True).data
