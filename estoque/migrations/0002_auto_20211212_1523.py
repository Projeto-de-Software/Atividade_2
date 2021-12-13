# Generated by Django 3.2.8 on 2021-12-12 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipocaixa',
            name='tipo',
            field=models.CharField(choices=[('C', 'Caixa'), ('P', 'Palet')], default='C', max_length=2),
        ),
        migrations.AlterField(
            model_name='tipocaixa',
            name='tipoCaixa',
            field=models.CharField(choices=[('PA', 'Papelão'), ('PL', 'Plástico')], default='PA', max_length=2),
        ),
    ]
