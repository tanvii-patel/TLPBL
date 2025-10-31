from django.db import models
from django.contrib.auth.models import User

DAYS = [
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday', 'Friday'),
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
]

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    day = models.CharField(max_length=20, choices=DAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ['day', 'start_time']

    def __str__(self):
        return f"{self.subject} ({self.day})"
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
class Resource(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='resources/files/', blank=True, null=True)
    image = models.ImageField(upload_to='resources/images/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title