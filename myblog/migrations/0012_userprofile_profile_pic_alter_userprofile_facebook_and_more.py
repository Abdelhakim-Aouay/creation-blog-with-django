# Generated by Django 4.2 on 2023-05-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0011_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profiles/'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]