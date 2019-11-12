# Generated by Django 2.2.6 on 2019-11-11 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_autorization_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solicitation',
            options={'verbose_name': 'Solicitação', 'verbose_name_plural': 'Solicitações'},
        ),
        migrations.RemoveField(
            model_name='solicitation',
            name='status',
        ),
        migrations.AlterField(
            model_name='autorization',
            name='status',
            field=models.CharField(choices=[('analise', 'Em Análise'), ('autorizado', 'Autorizado'), ('nao_autorizado', 'Não Autorizado')], default='analise', max_length=30, verbose_name='Status'),
        ),
    ]