# Generated by Django 4.2.6 on 2023-12-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DOS', '0006_student_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='division',
            field=models.CharField(choices=[('1', 'DIV1'), ('2', 'DIV2'), ('3', 'DIV3'), ('4', 'DIV4'), ('U', 'UNGRADED')], max_length=50),
        ),
        migrations.AlterField(
            model_name='position',
            name='std_class',
            field=models.CharField(choices=[('P1', 'P.0NE'), ('P2', 'P.TWO'), ('P3', 'P.THREE'), ('P4', 'P.FOUR'), ('P5', 'P.FIVE'), ('P6', 'P.SIX'), ('P7', 'P.SEVEN')], max_length=20),
        ),
        migrations.AlterField(
            model_name='position',
            name='stream',
            field=models.CharField(choices=[('A', 'EAST'), ('B', 'WEST')], max_length=30),
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='subject',
            field=models.CharField(choices=[('MATH', 'MATHEMATICS'), ('ENG', 'ENGLISH'), ('SCIE', 'SCIENCE'), ('SST', 'SOCIAL STUDIES')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='std_class',
            field=models.CharField(choices=[('P1', 'P.0NE'), ('P2', 'P.TWO'), ('P3', 'P.THREE'), ('P4', 'P.FOUR'), ('P5', 'P.FIVE'), ('P6', 'P.SIX'), ('P7', 'P.SEVEN')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='stream',
            field=models.CharField(choices=[('A', 'EAST'), ('B', 'WEST')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='term',
            field=models.CharField(choices=[('1', 'ONE'), ('2', 'TWO'), ('3', 'THREE')], max_length=20),
        ),
    ]
