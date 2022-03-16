from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.TextField()
    course_provider = models.TextField()
    course_completed = models.BooleanField()
    certificate_earned = models.TextField()

class Certification(models.Model):
    certification_name = models.TextField()
    certification_provider = models.TextField()
    date_earned = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()