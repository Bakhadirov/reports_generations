from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(blank=False)
    patronymic = models.CharField(max_length=100, blank=True)
    extra_information = models.TextField(blank=True)


class Events(models.Model):
    id = models.IntegerField(primary_key=True)
    install_time = models.DateTimeField()
    event_time = models.DateTimeField()
    appsflyer_id = models.CharField(max_length=255, blank=True)
    media_source = models.CharField(max_length=255, blank=True)
    campaign = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=255, blank=True)
    event_name = models.CharField(max_length=255, blank=True)
    event_revenue = models.DecimalField(max_digits=30, decimal_places=10, blank=True)
    event_revenue_usd = models.DecimalField(max_digits=30, decimal_places=10, blank=True)


    class Meta:
        db_table = 'events'


class Installs1(models.Model):
    id = models.IntegerField(primary_key=True)
    install_time = models.DateTimeField()
    event_time = models.DateTimeField()
    appsflyer_id = models.CharField(max_length=255, blank=True)
    media_source = models.CharField(max_length=255, blank=True)
    campaign = models.CharField(max_length=255, blank=True)
    platform = models.CharField(max_length=255, blank=True)
    event_name = models.CharField(max_length=255, blank=True)
    event_revenue = models.DecimalField(max_digits=30, decimal_places=20, blank=True)
    event_revenue_usd = models.DecimalField(max_digits=30, decimal_places=20, blank=True)

    class Meta:
        db_table = 'installs1'

