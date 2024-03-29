# Generated by Django 4.2.7 on 2024-03-08 13:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ticketmanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priority',
            options={'verbose_name_plural': 'Priority'},
        ),
        migrations.AlterModelOptions(
            name='slastatus',
            options={'verbose_name_plural': 'SLA Status'},
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.AlterField(
            model_name='incident',
            name='engineer_responsible',
            field=models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Engineer responsible'),
        ),
    ]
