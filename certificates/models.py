from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    student_name = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now_add=True)
    certificate_id = models.CharField(max_length=100, unique=True)
    issuer = models.ForeignKey(User, on_delete=models.CASCADE)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student_name} - {self.course_name}"