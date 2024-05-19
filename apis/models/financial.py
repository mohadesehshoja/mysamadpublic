from django.db import models

class Financial(models.Model):
    payment_amount = models.IntegerField(default=0)
    payment_date = models.DateField(auto_now_add=True)
    payment_id = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return "{}".format(self.payment_amount)






