# Generated by Django 4.0.2 on 2022-04-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_remove_book_id_book_author_book_book_id_book_images_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('laptop_id', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('brand', models.CharField(default='', max_length=100)),
                ('screensize', models.CharField(default='', max_length=100)),
                ('model', models.CharField(default='', max_length=100)),
                ('price', models.FloatField(default=0)),
                ('images', models.ImageField(default=None, null=b'I00\n', upload_to='image')),
            ],
        ),
    ]