# Generated by Django 5.0 on 2023-12-31 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cportal', '0013_alter_country_options_remove_companydirector_account_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='companydirector',
            options={'verbose_name': 'Associated with', 'verbose_name_plural': 'Associated with'},
        ),
        migrations.RenameField(
            model_name='company',
            old_name='phone',
            new_name='Phone Number',
        ),
        migrations.RenameField(
            model_name='director',
            old_name='phone',
            new_name='Phone Number',
        ),
    ]
