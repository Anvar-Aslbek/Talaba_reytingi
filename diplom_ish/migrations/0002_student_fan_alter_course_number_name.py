# Generated by Django 4.0.4 on 2022-05-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diplom_ish', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fan',
            field=models.ManyToManyField(to='diplom_ish.subject'),
        ),
        migrations.AlterField(
            model_name='course_number',
            name='name',
            field=models.IntegerField(),
        ),
    ]
