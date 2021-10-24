# Generated by Django 3.1.3 on 2021-10-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Binary', 'Binary')], max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('town', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
