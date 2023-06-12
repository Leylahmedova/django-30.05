# Generated by Django 3.2 on 2023-06-12 12:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20230609_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('image', models.ImageField(upload_to='')),
                ('company_image', models.ImageField(upload_to='')),
            ],
        ),
    ]