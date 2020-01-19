from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Operation(models.Model):
    POSTING_KEYS = (
        (0, 'Wydatek'),
        (1, 'Zasilenie'),
    )
    date_added = models.DateTimeField(default=timezone.now)
    date_operation = models.DateField(default=timezone.now)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.CharField(max_length=50)
    posting_key = models.IntegerField(default=0, choices=POSTING_KEYS)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.date_operation) + ": " + self.description + " (" + str(self.amount) + ")"

    def get_absolute_url(self):
        return reverse('wallet-home')
