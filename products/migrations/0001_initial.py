# Generated by Django 3.0.8 on 2020-10-31 19:28

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Garment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='static/images')),
                ('img_path', models.CharField(max_length=100)),
                ('brand_name', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=19)),
                ('name', models.CharField(max_length=100)),
                ('fabric', models.CharField(max_length=30)),
                ('category', multiselectfield.db.fields.MultiSelectField(choices=[('Men', "Men's Wear"), ('Women', "Women's Wear"), ('Infant', 'Baby wear'), ('Boy', 'Boys wear'), ('Girl', 'Girls Wear')], max_length=25)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GarmentSubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'GarmentSubcategories',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name_plural': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clothing', models.ManyToManyField(to='products.Garment')),
            ],
        ),
        migrations.CreateModel(
            name='GarmentDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specific_name', models.CharField(max_length=100)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=20)),
                ('height', models.DecimalField(decimal_places=2, max_digits=20)),
                ('width', models.DecimalField(decimal_places=2, max_digits=20)),
                ('depth', models.DecimalField(decimal_places=2, max_digits=20)),
                ('colors', models.CharField(max_length=150)),
                ('material', models.CharField(max_length=100)),
                ('is_discounted', models.BooleanField(default=False)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=True)),
                ('pockets_qty', models.IntegerField(blank=True, default=1)),
                ('zip_qty', models.IntegerField(blank=True, default=0)),
                ('description', models.TextField(blank=True)),
                ('suitable_season', multiselectfield.db.fields.MultiSelectField(choices=[('Rainy', 'Rainy'), ('Spring', 'Spring'), ('Winter', 'Winter'), ('Autumn', 'Autumn'), ('Summer', 'Summer')], max_length=33)),
                ('neck_design', models.CharField(choices=[('Round', 'Round'), ('V-neck', 'V-neck'), ('PoloCollar', 'PoloCollar')], default='Round', max_length=20)),
                ('subcategory', models.ManyToManyField(to='products.GarmentSubcategory')),
            ],
            options={
                'verbose_name_plural': 'GarmentDetails',
            },
        ),
        migrations.AddField(
            model_name='garment',
            name='garment_details',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.GarmentDetails'),
        ),
        migrations.AddField(
            model_name='garment',
            name='store',
            field=models.ManyToManyField(to='stores.Store'),
        ),
    ]
