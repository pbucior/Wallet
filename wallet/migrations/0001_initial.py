# Generated by Django 3.0.2 on 2020-01-18 20:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_operation', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(max_length=50)),
                ('posting_key', models.IntegerField(choices=[(0, 'Winien'), (1, 'Ma')], default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
