from django.db import models

# Create your models here.
class Diary(models.Model):
    diary_title = models.CharField(max_length=200, default='', null=True)
    diary_editor = models.TextField()
    diary_time_created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.diary_title