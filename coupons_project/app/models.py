from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class Coupon(models.Model):
    service = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])
    start_data = models.DateTimeField()
    end_data = models.DateTimeField()
    limit = used = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )
    used = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.code


class CheckoutItem(models.Model):
    date_time = models.DateTimeField()
    amont = models.IntegerField(
        default=0,
        blank=False,
        null=False,
    )
    currency = models.CharField(max_length=100)

