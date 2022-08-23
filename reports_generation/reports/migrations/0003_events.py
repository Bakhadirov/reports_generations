# Generated by Django 4.1 on 2022-08-21 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_installs1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name='ID',
                    ),
                ),
                ('install_time', models.DateTimeField(verbose_name=models.Model)),
                ('event_time', models.DateTimeField()),
                ('appsflyer_id', models.CharField(blank=True, max_length=255)),
                ('media_source', models.CharField(blank=True, max_length=255)),
                ('campaign', models.CharField(blank=True, max_length=255)),
                ('platform', models.CharField(blank=True, max_length=255)),
                ('event_name', models.CharField(blank=True, max_length=255)),
                (
                    'event_revenue',
                    models.DecimalField(blank=True, decimal_places=20, max_digits=30),
                ),
                (
                    'event_revenue_usd',
                    models.DecimalField(blank=True, decimal_places=20, max_digits=30),
                ),
            ],
        ),
    ]