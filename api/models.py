from django.db import models
from .utils import generate_ref_code


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    telephone = models.CharField(max_length=11, null=False, blank=False)
    recommended_by = models.ForeignKey('self', null=True, blank=False, on_delete=models.SET_NULL, related_name='ref_by')
    code = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.name}-{self.code}"

    def get_recommended_by(self):
        return self.recommended_by

    def save(self, *args, **kwargs):
        if self.code == "":
            cond = True
            while cond:
                code = generate_ref_code()
                if not Student.objects.all().filter(code=code).exists():
                    cond = False
            self.code = code
        super().save(*args, **kwargs)
