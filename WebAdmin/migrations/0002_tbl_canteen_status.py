# Generated by Django 5.1.6 on 2025-02-20 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAdmin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_canteen',
            name='status',
            field=models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1),
        ),
    ]
