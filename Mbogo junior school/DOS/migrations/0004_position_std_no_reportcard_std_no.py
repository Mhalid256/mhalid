# Generated by Django 4.2.6 on 2023-12-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOS', '0003_grading_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='std_No',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='reportcard',
            name='std_No',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
