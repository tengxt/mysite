# Generated by Django 2.0 on 2019-01-05 13:16

from django.db import migrations
import mdeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=mdeditor.fields.MDTextField(),
        ),
    ]
