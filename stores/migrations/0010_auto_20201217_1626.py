# Generated by Django 3.1.2 on 2020-12-17 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0009_auto_20201217_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storedetails',
            name='popularity',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='stores.popularity'),
        ),
    ]
