# Generated by Django 4.1.7 on 2023-06-16 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autobazar', '0008_alter_zamestnanec_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='autobazar',
            name='fotka',
            field=models.ImageField(blank=True, help_text='Nahrejte logo autobazaru', null=True, upload_to='autobazary', verbose_name='Logo autobazaru'),
        ),
    ]