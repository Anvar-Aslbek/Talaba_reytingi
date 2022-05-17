# Generated by Django 4.0.4 on 2022-05-17 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diplom_ish', '0002_student_fan_alter_course_number_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Talaba', 'verbose_name_plural': 'Talabalar'},
        ),
        migrations.AddField(
            model_name='student',
            name='holat',
            field=models.CharField(default='baho', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='faculty_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.faculty', verbose_name='Fakulteti'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=100, verbose_name='Ism'),
        ),
        migrations.AlterField(
            model_name='student',
            name='kurs_number_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diplom_ish.course_number', verbose_name='kursi'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=100, verbose_name='Familiya'),
        ),
        migrations.AlterField(
            model_name='student',
            name='tel_number',
            field=models.CharField(max_length=100, verbose_name='phone_number'),
        ),
    ]