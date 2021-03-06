# Generated by Django 3.1.3 on 2021-02-04 13:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('middle_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_no', models.IntegerField()),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('github', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(choices=[('PhD', 'PhD'), ('Mtech/MA/MSc/MCom/MBA', 'Masters'), ('BE/Btech/BA/BSc/BCom', 'Bachelors'), ('12th', 'High School')], max_length=25)),
                ('institution', models.CharField(max_length=75)),
                ('board', models.CharField(max_length=75)),
                ('start_yr', models.DateField()),
                ('end_yr', models.DateField()),
                ('cgpa', models.IntegerField(blank=True)),
                ('percent', models.IntegerField(blank=True)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_maker.person')),
            ],
        ),
    ]
