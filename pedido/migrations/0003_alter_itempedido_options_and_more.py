# Generated by Django 4.1.3 on 2022-11-24 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0002_rename_variacao_itempedido_variação_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='itempedido',
            options={'verbose_name': 'Item do pedido', 'verbose_name_plural': 'Itens do pedido'},
        ),
        migrations.RenameField(
            model_name='itempedido',
            old_name='image',
            new_name='imagem',
        ),
        migrations.RenameField(
            model_name='itempedido',
            old_name='variação',
            new_name='variacao',
        ),
        migrations.RenameField(
            model_name='itempedido',
            old_name='variação_id',
            new_name='variacao_id',
        ),
        migrations.AddField(
            model_name='pedido',
            name='qtd_total',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
