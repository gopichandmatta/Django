from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    blood_group = models.CharField(max_length=5)

    def __str__(self):
        return self.name
