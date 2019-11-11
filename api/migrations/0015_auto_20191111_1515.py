# Generated by Django 2.2.6 on 2019-11-11 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_autorization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autorization',
            name='solicitation',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='autorization', to='api.Solicitation'),
        ),
        migrations.AlterField(
            model_name='solicitation',
            name='status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Autorizado'), (2, 'Não Autorizado')], null=True),
        ),
    ]
