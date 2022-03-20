from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.TextField()
    course_provider = models.TextField()
    course_completed = models.BooleanField()
    certificate_earned = models.TextField()
    def __str__(self):
        return self.course_name, self.course_provider, self.course_completed, self.certificate_earned

class Certification(models.Model):
    certification_name = models.TextField()
    certification_provider = models.TextField()
    date_earned = models.DateField(auto_now_add=True)
    expiration_date = models.DateField()
    def __str__(self):
        return self.certification_name, self.certification_provider