# Generated by Django 3.0.6 on 2020-05-30 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bitly', '0002_bitlinklog'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitlinklog',
            name='http_meta_json',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bitlinklog',
            name='http_referer',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='bitlinklog',
            name='http_remote_address',
            field=models.CharField(blank=True, max_length=31, null=True),
        ),
        migrations.AddField(
            model_name='bitlinklog',
            name='http_user_agent',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
