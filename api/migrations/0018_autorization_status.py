# Generated by Django 2.2.6 on 2019-11-11 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20191111_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='autorization',
            name='status',
            field=models.CharField(choices=[('analise', 'Em Análise'), ('autorizado', 'Autorizado'), ('nao_autorizado', 'Não Autorizado')], default='analise', max_length=30),
        ),
    ]
