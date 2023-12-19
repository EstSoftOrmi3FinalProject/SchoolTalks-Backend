from django.db import models

class Inquiry(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return f"{self.subject} - {self.email}"
