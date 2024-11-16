# Generated by Django 3.2.5 on 2024-11-16 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_auto_20211109_1456'),
        ('shifts', '0004_auto_20241116_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busshift',
            name='bus',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fleet.bus'),
        ),
        migrations.AlterField(
            model_name='busshift',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fleet.driver'),
        ),
    ]
