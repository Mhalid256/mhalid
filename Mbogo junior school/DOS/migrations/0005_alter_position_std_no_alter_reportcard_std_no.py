# Generated by Django 4.2.6 on 2023-12-20 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DOS', '0004_position_std_no_reportcard_std_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='std_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOS.student'),
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='std_No',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DOS.student'),
        ),
    ]
