# Generated by Django 5.0.6 on 2024-08-27 07:59

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0011_learningcenter_usertype'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='userType',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='login',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teacher',
            name='userType',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='learningcenter',
            name='login',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='learningcenter',
            name='password',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='login',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(max_length=250),
        ),
    ]
