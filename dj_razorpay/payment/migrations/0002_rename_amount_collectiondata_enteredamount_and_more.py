# Generated by Django 4.2.7 on 2023-12-01 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectiondata',
            old_name='amount',
            new_name='enteredAmount',
        ),
        migrations.RenameField(
            model_name='donar_data',
            old_name='amount',
            new_name='enteredAmount',
        ),
        migrations.RenameField(
            model_name='donation',
            old_name='amount',
            new_name='enteredAmount',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]