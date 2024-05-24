from django.db import models

from apis.models.abstract import TimeStampedModel
from .user import User


class Profile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    full_name = models.CharField(max_length=120)
    student_id = models.IntegerField()
    id_number = models.IntegerField()
    city = models.CharField(max_length=120, null=True)
    phone = models.CharField(max_length=120)
    email = models.EmailField(null=True)

    def __str__(self):
        return "{}".format(self.full_name)
