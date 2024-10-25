# Generated by Django 5.0.7 on 2024-10-17 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operator', models.CharField(choices=[('SFR', 'SFR'), ('Bouygues', 'Bouygues'), ('Orange', 'Orange')], max_length=10)),
                ('service', models.CharField(choices=[('Internet', 'Internet'), ('Telephony', 'Telephony'), ('Both', 'Both')], max_length=10)),
                ('client_name', models.CharField(max_length=100)),
                ('dhcp', models.CharField(max_length=100)),
                ('ip_private', models.CharField(blank=True, max_length=15, null=True)),
                ('ip_public', models.CharField(blank=True, max_length=15, null=True)),
                ('interco', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]