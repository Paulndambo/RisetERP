# Generated by Django 3.1.3 on 2021-10-24 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_report_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='documents')),
                ('date_uploaded', models.DateField(auto_now=True)),
            ],
        ),
    ]
