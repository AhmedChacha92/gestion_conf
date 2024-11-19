# Generated by Django 5.0.7 on 2024-11-05 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configurations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='dhcp',
            field=models.GenericIPAddressField(protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='interco',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='ip_private',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
        migrations.AlterField(
            model_name='configuration',
            name='ip_public',
            field=models.GenericIPAddressField(blank=True, null=True, protocol='IPv4'),
        ),
    ]