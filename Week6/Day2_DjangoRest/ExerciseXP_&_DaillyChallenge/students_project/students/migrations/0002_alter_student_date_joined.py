# Generated by Django 4.2.4 on 2023-08-14 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_joined',
            field=models.DateTimeField(),
        ),
    ]