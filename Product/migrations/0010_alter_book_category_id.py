# Generated by Django 4.0.2 on 2022-04-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0009_alter_book_category_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='category_id',
            field=models.ForeignKey(null=None, on_delete=django.db.models.deletion.CASCADE, to='Product.category'),
        ),
    ]
