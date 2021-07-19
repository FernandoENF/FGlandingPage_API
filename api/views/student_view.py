from rest_framework.views import APIView
from ..services import student_service
from ..serializers import student_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import student


class StudentList(APIView):
    def get(self, request, format=None):
        students = student_service.list_students()
        serializer = student_serializer.StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = student_serializer.StudentSerializer(data=request.data)
        if serializer.is_valid():
            ref_code = serializer.validated_data['ref_code']
            if ref_code is not None:
                name = serializer.validated_data["name"]
                email = serializer.validated_data["email"]
                telephone = serializer.validated_data["telephone"]
                code = ""
                recommended_by = student_service.get_student_by_code(ref_code)
                new_student = student.Student(name=name, email=email, telephone=telephone, code=code,
                                              recommended_by=recommended_by)
                student_bd = student_service.add_student(new_student)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                name = serializer.validated_data["name"]
                email = serializer.validated_data["email"]
                telephone = serializer.validated_data["telephone"]
                code = ""
                recommended_by = None
                new_student = student.Student(name=name, email=email, telephone=telephone, code=code,
                                              recommended_by=recommended_by)
                student_bd = student_service.add_student(new_student)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


