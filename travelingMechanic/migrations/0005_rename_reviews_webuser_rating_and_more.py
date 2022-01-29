# Generated by Django 4.0.1 on 2022-01-29 19:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelingMechanic', '0004_webuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='webuser',
            old_name='reviews',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='commission',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelingMechanic.webuser'),
        ),
        migrations.AlterField(
            model_name='commission',
            name='description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stars', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('image', models.ImageField(blank=True, upload_to='reviewspic/')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travelingMechanic.webuser')),
            ],
        ),
    ]
