# Generated by Django 2.2.6 on 2019-11-12 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20191111_2024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitation',
            options={'ordering': ['-autorization__status'], 'verbose_name': 'Solicitação', 'verbose_name_plural': 'Solicitações'},
        ),
    ]
