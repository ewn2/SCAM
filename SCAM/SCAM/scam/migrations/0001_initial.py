# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-15 02:34
from __future__ import unicode_literals

import SCAM.scam.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveCourse',
            fields=[
                ('cid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=10)),
                ('section', models.IntegerField()),
                ('term', models.CharField(choices=[('Fall', 'Fall'), ('Winter', 'Winter'), ('Spring', 'Spring'), ('Summer', 'Summer')], max_length=6)),
                ('year', models.IntegerField(default=2017, validators=[django.core.validators.MinValueValidator(2000), django.core.validators.MaxValueValidator(2018)])),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='CurrentCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.ActiveCourse')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='FutureCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=SCAM.scam.models.get_image_path)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, default=-1, max_digits=2, null=True)),
                ('years_exp_total', models.IntegerField(blank=True, default=0, null=True)),
                ('years_exp_sjsu', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PastCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.CharField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Course')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=9)),
                ('name', models.CharField(max_length=70)),
                ('bio', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to=SCAM.scam.models.get_image_path)),
                ('student_year', models.CharField(choices=[('Freshman', 'Freshman'), ('Sophomore', 'Sophomore'), ('Junior', 'Junior'), ('Senior', 'Senior'), ('1st Year Graduate', '1st Year Graduate'), ('2nd Year Graduate', '2nd Year Graduate'), ('1st Year PhD', '1st Year PhD'), ('2nd Year PhD', '2nd Year PhD'), ('3rd Year PhD', '3rd Year PhD'), ('4th Year PhD', '4th Year PhD')], max_length=17)),
                ('days_joined', models.IntegerField(blank=True, default=0, null=True)),
                ('days_active', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Student'),
        ),
        migrations.AddField(
            model_name='pastcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Student'),
        ),
        migrations.AddField(
            model_name='futurecourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Student'),
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendB', to='scam.Student'),
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friendA', to='scam.Student'),
        ),
        migrations.AddField(
            model_name='currentcourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Student'),
        ),
        migrations.AddField(
            model_name='activecourse',
            name='instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scam.Instructor'),
        ),
    ]