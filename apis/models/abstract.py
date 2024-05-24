from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['created']


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BasePayment(models.Model):
    payment_amount = models.IntegerField()
    payment_date = models.DateField(auto_now_add=True)
    payment_id = models.IntegerField()

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.payment_amount)
