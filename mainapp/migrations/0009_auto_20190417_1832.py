# Generated by Django 2.1.5 on 2019-04-17 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20190414_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='journal',
            field=models.ForeignKey(blank=True, default='', help_text="IMPORTANT: If your journal isn't listed here, go to the bottom of the form and click 'Add Journal'. After you create the new Journal entry, you will be returned to this form.", null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.Journal'),
        ),
    ]
