# Generated by Django 4.2.1 on 2023-05-30 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageCompressor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='iamge_compressor', verbose_name='Изобрадение')),
            ],
            options={
                'verbose_name': 'Изобпажение',
                'verbose_name_plural': 'Изобпажения',
                'db_table': 'image__compress',
            },
        ),
    ]
