from django.db import models


class Profile(models.Model):
    full_name = models.CharField(max_length=120)
    student_id = models.IntegerField()

    def __str__(self):
        return "{}".format(self.full_name)
