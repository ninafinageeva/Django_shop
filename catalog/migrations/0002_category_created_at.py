# Generated by Django 5.0.4 on 2024-04-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='будет отменено'),
        ),
    ]
