# Generated by Django 4.1.2 on 2022-10-06 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_bio_user_name_alter_user_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hackathon_participant',
            field=models.BooleanField(default=True),
        ),
    ]
