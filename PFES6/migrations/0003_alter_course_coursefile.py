# Generated by Django 3.2.3 on 2021-05-31 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PFES6', '0002_alter_classsubject_codeclasse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='courseFile',
            field=models.FileField(null=True, upload_to='documents'),
        ),
    ]
