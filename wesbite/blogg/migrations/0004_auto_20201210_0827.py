# Generated by Django 3.1.4 on 2020-12-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0003_auto_20201209_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_image',
            field=models.ImageField(blank=True, null=True, upload_to='blogg/static/blogg/images/'),
        ),
    ]
