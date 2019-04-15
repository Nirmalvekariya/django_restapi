from django.db import models


class Tasks(models.Model):
    Task_Name = models.CharField(max_length=50)
    Task_Description = models.CharField(max_length=50)

    def __str__(self):
        return self.name