# Generated by Django 5.0.6 on 2024-08-06 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LearningCenter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('appeal_phone_number', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='learning_center_images/')),
                ('location', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('manager_name', models.CharField(max_length=255)),
                ('manager_phone_number', models.CharField(max_length=15)),
            ],
        ),
    ]
