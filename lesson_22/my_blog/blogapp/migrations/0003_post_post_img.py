# Generated by Django 4.1.7 on 2023-03-16 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_img',
            field=models.ImageField(blank=True, null=True, upload_to='blogapp'),
        ),
    ]