# Generated by Django 3.1.2 on 2023-03-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20230307_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='teacher',
            field=models.ManyToManyField(related_name='teacher', to='school.Teacher'),
        ),
    ]
