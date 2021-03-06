# Generated by Django 4.0.1 on 2022-01-21 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('protocol', '0002_protocol_protocol_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='clerk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='department.department'),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='note',
            field=models.TextField(blank=True),
        ),
    ]
