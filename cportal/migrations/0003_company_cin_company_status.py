# Generated by Django 5.0 on 2023-12-31 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cportal', '0002_country_company_country_state_company_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cin',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('ACT', 'ACTIVE'), ('DRM', 'DORMANT'), ('INAC', 'INACTIVE'), ('DRFT', 'DRAFT')], default='DRAFT', max_length=30),
        ),
    ]
