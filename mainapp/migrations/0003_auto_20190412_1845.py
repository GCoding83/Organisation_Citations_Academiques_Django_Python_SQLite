# Generated by Django 2.1.5 on 2019-04-12 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_auto_20190410_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, help_text='Optional. If author only has one name (e.g. Aristotle), enter it as a last name', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='last_name',
            field=models.CharField(help_text='Required.', max_length=30),
        ),
        migrations.AlterField(
            model_name='author',
            name='middle_name',
            field=models.CharField(blank=True, help_text='Optional.', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
    ]