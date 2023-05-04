# Generated by Django 4.1.5 on 2023-05-04 12:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('weight', models.PositiveIntegerField()),
                ('fats_count', models.PositiveIntegerField()),
                ('protein_count', models.PositiveIntegerField()),
                ('carbohydrates_count', models.PositiveIntegerField()),
                ('calories_count', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('name', models.CharField(max_length=256)),
                ('products', models.ManyToManyField(to='web.product')),
            ],
        ),
        migrations.CreateModel(
            name='CaloriesLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('meals', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.meal')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
