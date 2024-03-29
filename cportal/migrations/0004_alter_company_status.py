# Generated by Django 5.0 on 2023-12-31 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cportal', '0003_company_cin_company_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='status',
            field=models.CharField(choices=[('ACT', 'ACTIVE'), ('DRM', 'DORMANT'), ('INAC', 'INACTIVE'), ('DRFT', 'DRAFT')], default='DRAFT', max_length=15),
        ),
    ]
