# Generated by Django 4.0.1 on 2022-01-30 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelingMechanic', '0011_review_author_alter_review_target'),
    ]

    operations = [
        migrations.AddField(
            model_name='commission',
            name='done',
            field=models.BooleanField(default=False),
        ),
    ]
