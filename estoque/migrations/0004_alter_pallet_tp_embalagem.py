# Generated by Django 3.2.8 on 2022-03-28 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_alter_pallet_sn_sobra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pallet',
            name='tp_embalagem',
            field=models.CharField(choices=[('PA', 'PAPELÃO'), ('PL', 'PLÁSTICO')], max_length=10),
        ),
    ]