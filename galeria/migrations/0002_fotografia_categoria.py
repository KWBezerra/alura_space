# Generated by Django 5.0.6 on 2024-07-24 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'estrela'), ('GALÁXIA', 'galáxia'), ('PLANETA', 'planeta')], default='', max_length=100),
        ),
    ]
