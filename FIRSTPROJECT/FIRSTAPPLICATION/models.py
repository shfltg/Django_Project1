from django.db import models

# Create your models here. name,id,contact, address
class Candidates(models.Model):
    Name=models.CharField(max_length=10)
    Id = models.IntegerField()
    Contact = models.IntegerField()
    Address = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.Name