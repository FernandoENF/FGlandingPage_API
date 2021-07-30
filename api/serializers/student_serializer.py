from rest_framework import serializers
from ..models import Student
from ..services import student_service


def ref_code_validate(ref_code):
    if student_service.check_code(ref_code):
        return ref_code
    raise serializers.ValidationError("Codigo invalido!")


class StudentSerializer(serializers.ModelSerializer):
    ref_code = serializers.CharField(max_length=12, write_only=True,
                                     required=True, allow_null=True,
                                     validators=[ref_code_validate])

    code = serializers.CharField(read_only=True)

    class Meta:
        model = Student
        fields = ('name', 'email', 'telephone', 'code', 'ref_code')

    def validate_email(self, email):
        if student_service.check_email(email):
            return email
        raise serializers.ValidationError('Email ja inscrito!')
