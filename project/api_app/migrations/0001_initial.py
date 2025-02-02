# Generated by Django 5.1.1 on 2024-09-10 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='название')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='цена')),
            ],
        ),
    ]
