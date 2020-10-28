from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    Title = models.CharField(max_length=200)
    CourseNumber = models.IntegerField
    InstructorName = models.CharField(max_length=200)
    Duration = models.FloatField

    def __str__(self):
        return self.Title


