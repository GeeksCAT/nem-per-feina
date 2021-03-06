# Generated by Django 3.0.7 on 2020-11-04 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsapp', '0017_auto_20201104_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(blank=True, default=None, help_text='Minimum and maximum annual salary for this job. Examples: 30.000 €, 30.000 € - 40.000 €, etc', max_length=50, null=True, verbose_name='Salary'),
        ),
    ]
