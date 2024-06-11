# Generated by Django 5.0.6 on 2024-06-11 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.TextField()),
                ('file', models.FileField(upload_to='file/')),
                ('image', models.ImageField(upload_to='images/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status_of_task', models.CharField(max_length=50)),
            ],
        ),
    ]
