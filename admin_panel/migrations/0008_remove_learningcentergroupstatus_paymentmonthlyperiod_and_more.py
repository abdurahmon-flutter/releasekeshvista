# Generated by Django 5.0.6 on 2024-08-24 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0007_rename_dailypayment_learningcentergroupstatus_paymentamount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='learningcentergroupstatus',
            name='paymentMonthlyPeriod',
        ),
        migrations.AddField(
            model_name='learningcentergroupstatus',
            name='nextPaymentMonth',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learningcentergroupstatus',
            name='nextPaymentYear',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='learningcentergroupstatus',
            name='paymentPeriod',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
