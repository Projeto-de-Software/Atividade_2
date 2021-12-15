# Generated by Django 3.2.8 on 2021-12-15 03:11

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0004_alter_produto_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='codigoInterno',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='produto',
            name='embalagem',
            field=models.CharField(choices=[('GARRAFA', 'GARRAFA'), ('UNIDADE', 'UNIDADE'), ('BANDEJA', 'BANDEJA'), ('BALDE', 'BALDE'), ('LITRO', 'LITRO'), ('QUILOGRAMA', 'QUILOGRAMA')], default='UNIDADE', max_length=20),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidadeCaixa',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='superPalet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoBarras', models.CharField(max_length=20, unique=True)),
                ('dataCriacao', models.DateField(default=django.utils.timezone.now)),
                ('dataArmazenamento', models.DateField(blank=True, null=True)),
                ('quantidadeItens', models.IntegerField(default=1)),
                ('tipoEmbalagem', models.CharField(choices=[('PA', 'Papelão'), ('PL', 'Plástico')], default='PA', max_length=2)),
                ('paleteria', models.IntegerField()),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estoque.produto')),
            ],
        ),
    ]