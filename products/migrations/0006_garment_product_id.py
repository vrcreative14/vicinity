# Generated by Django 3.1.2 on 2021-02-04 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_garment_qrcode_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='garment',
            name='product_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
