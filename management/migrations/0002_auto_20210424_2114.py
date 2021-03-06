# Generated by Django 3.2 on 2021-04-24 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospitals',
            old_name='bed_count',
            new_name='total_beds',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='added_by',
        ),
        migrations.RemoveField(
            model_name='hospitals',
            name='oxygen_count',
        ),
        migrations.AddField(
            model_name='hospitals',
            name='city',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospitals',
            name='contact_info',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='ventilator_availability',
            field=models.BooleanField(default=False),
        ),
    ]
