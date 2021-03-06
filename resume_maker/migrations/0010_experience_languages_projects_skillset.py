# Generated by Django 3.1.3 on 2021-02-04 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('resume_maker', '0009_auto_20210204_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='SkillSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=25)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_maker.person')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=150)),
                ('start_dt', models.DateField()),
                ('end_dt', models.DateField()),
                ('project_link', models.URLField(blank=True, null=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_maker.person')),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=25)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_maker.person')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=150)),
                ('join_dt', models.DateField()),
                ('left_dt', models.DateField()),
                ('details', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_maker.person')),
            ],
        ),
    ]
