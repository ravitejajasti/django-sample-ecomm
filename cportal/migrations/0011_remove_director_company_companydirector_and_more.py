# Generated by Django 5.0 on 2023-12-31 05:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cportal', '0010_alter_director_address_alter_director_din_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='director',
            name='company',
        ),
        migrations.CreateModel(
            name='CompanyDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cportal.director')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cportal.company')),
            ],
        ),
        migrations.AddField(
            model_name='director',
            name='company',
            field=models.ManyToManyField(through='cportal.CompanyDirector', to='cportal.company'),
        ),
    ]