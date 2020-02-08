# Generated by Django 3.0.2 on 2020-02-05 16:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('num_profiles', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('level_edu', models.CharField(choices=[('undergraduate', 'Under Graduate'), ('graduate', 'Graduate')], default='graduate', max_length=20)),
                ('prof', models.CharField(max_length=100)),
                ('bio', models.TextField(max_length=100)),
                ('is_reserved', models.BooleanField()),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Country')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.Gender')),
            ],
        ),
    ]
