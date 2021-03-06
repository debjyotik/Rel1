# Generated by Django 3.1.5 on 2021-03-10 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_fname', models.CharField(max_length=255, verbose_name='First Name')),
                ('patient_lname', models.CharField(max_length=255, verbose_name='Last Name')),
                ('age', models.FloatField(verbose_name='Age of Patient')),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male')], max_length=11)),
                ('ailment', models.CharField(max_length=1000, verbose_name='Ailment')),
                ('patient_report', models.FileField(blank=True, upload_to='')),
            ],
        ),
    ]
