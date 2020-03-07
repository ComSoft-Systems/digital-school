# Generated by Django 3.0.3 on 2020-03-07 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dependencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('exam_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('exam_session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dependencies.Session')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('semester_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('semester_name', models.CharField(max_length=30, verbose_name='semester')),
                ('exam_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
            ],
        ),
        migrations.CreateModel(
            name='Semesterbreakup',
            fields=[
                ('semesterbreakup_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('semesterbreakup_name', models.CharField(max_length=30, verbose_name='semester-breakup')),
                ('exam_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
                ('semester_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Quater',
            fields=[
                ('quater_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('quater_name', models.CharField(max_length=30, verbose_name='Quater')),
                ('exam_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
                ('semester_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Semester')),
                ('semesterbreakup_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Semesterbreakup')),
            ],
        ),
        migrations.CreateModel(
            name='Assesment',
            fields=[
                ('assesment_code', models.IntegerField(auto_created=True, primary_key=True, serialize=False, unique=True)),
                ('assesment_name', models.CharField(max_length=30, verbose_name='Quater')),
                ('exam_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Exam')),
                ('quater_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Quater')),
                ('semester_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Semester')),
                ('semesterbreakup_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.Semesterbreakup')),
            ],
        ),
    ]
