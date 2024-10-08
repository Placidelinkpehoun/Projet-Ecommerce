# Generated by Django 5.0.7 on 2024-08-14 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_remove_commande_produit_commande_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='id_categorie',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='img_categorie',
            field=models.ImageField(blank=True, null=True, upload_to='front/images/category/'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='img_produit',
            field=models.ImageField(blank=True, null=True, upload_to='front/images/grocery/'),
        ),
    ]
