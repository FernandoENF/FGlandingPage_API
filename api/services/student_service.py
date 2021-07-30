from ..models import Student


def list_students():
    students = Student.objects.all()
    return students


def add_student(student):
    return Student.objects.create(name=student.name, email=student.email, telephone=student.telephone,
                                  recommended_by=student.recommended_by, code=student.code)


def check_email(email):
    try:
        match = Student.objects.get(email=email)
    except Student.DoesNotExist:
        return True
    return False


def check_code(ref_code):
    try:
        student = Student.objects.get(code=ref_code)
    except Student.DoesNotExist:
        student = None
    if student is not None:
        return True
    else:
        return False


def get_student_by_code(ref_code):
    student = Student.objects.get(code=ref_code)
    return student
