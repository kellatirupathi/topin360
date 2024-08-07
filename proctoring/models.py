import uuid
from django.db import models


# Create your models here.
class Assessment(models.Model):
    assessment_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Student(models.Model):
    student_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Video(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        print('----[Video Saved]----')
        super(Video, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.timestamp)

    class Meta:
        ordering = ["-timestamp"]
