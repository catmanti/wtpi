# Generated by Django 4.0.4 on 2022-05-21 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=models.CharField(default='catman', max_length=200),
            preserve_default=False,
        ),
    ]