# Generated by Django 4.2.4 on 2023-08-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_alter_student_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
