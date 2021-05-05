from django.db import models

# Create your models here.
class Blog(models.Model):
    subject = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    date = models.DateTimeField()
    content = models.TextField()

    def __str__(self):
        return self.subject

    def brief(self):
        return self.content[:500]


