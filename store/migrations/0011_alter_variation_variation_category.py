# Generated by Django 4.2.5 on 2023-09-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_product_tax_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('taille', 'taille'), ('couleur', 'couleur')], max_length=100),
        ),
    ]