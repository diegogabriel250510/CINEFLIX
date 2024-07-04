# Generated by Django 5.0.6 on 2024-07-03 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0005_alter_filme_categorias'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filme',
            name='categorias',
        ),
        migrations.AddField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('DR', 'drama'), ('C', 'comedia'), ('R', 'romance'), ('DOC', 'documentario'), ('AC', 'ação'), ('AV', 'aventura'), ('FC', 'ficção cientifica'), ('T', 'Terror')], default=True, max_length=3),
            preserve_default=False,
        ),
    ]
