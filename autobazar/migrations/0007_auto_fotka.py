# Generated by Django 4.1.7 on 2023-06-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autobazar', '0006_zamestnanec_autobazar'),
    ]

    operations = [
        migrations.AddField(
            model_name='auto',
            name='fotka',
            field=models.ImageField(blank=True, help_text='Nahrejte fotku auta', null=True, upload_to='auta', verbose_name='Fotka auta'),
        ),
    ]