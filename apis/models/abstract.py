from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class BasePayment(models.Model):
    payment_amount = models.IntegerField(null=True, blank=True)
    payment_date = models.DateField(auto_now_add=True, null=True, blank=True)
    payment_id = models.IntegerField(null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{}".format(self.payment_amount)
