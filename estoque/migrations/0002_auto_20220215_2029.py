# Generated by Django 3.2.8 on 2022-02-15 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloco',
            name='sn_deletado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='paleteira',
            name='sn_deletado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='produto',
            name='sn_deletado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rua',
            name='sn_deletado',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ruaproduto',
            name='sn_deletado',
            field=models.BooleanField(default=False),
        ),
    ]
