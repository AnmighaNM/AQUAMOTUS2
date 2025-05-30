# Generated by Django 5.1.6 on 2025-02-20 04:16

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('StationMaster', '0001_initial'),
        ('WebAdmin', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Concession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('id_card', models.ImageField(blank=True, null=True, upload_to='id_cards/')),
                ('aadhar_card', models.ImageField(blank=True, null=True, upload_to='id_cards/')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(default='pending', max_length=50)),
                ('end_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='end_concessions', to='WebAdmin.tbl_district')),
                ('start_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_concessions', to='WebAdmin.tbl_district')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('reply', models.TextField(blank=True, null=True)),
                ('status', models.IntegerField(default=0)),
                ('sentiment_score', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_eventbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateField()),
                ('event_starttime', models.TimeField(default=datetime.time(0, 0))),
                ('duration', models.DurationField(blank=True, null=True)),
                ('event_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('adult_count', models.CharField(max_length=20)),
                ('children_count', models.CharField(max_length=20)),
                ('boat_deck', models.CharField(default='1', max_length=50)),
                ('status', models.IntegerField(default=0)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('assign', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='WebAdmin.tbl_boat')),
                ('event_endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_endpoints', to='WebAdmin.tbl_place')),
                ('event_startpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_startpoints', to='WebAdmin.tbl_place')),
                ('event_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='WebAdmin.tbl_eventtype')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_ticketbooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('ticket_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('adults_count', models.CharField(max_length=20)),
                ('childrens_count', models.CharField(max_length=20)),
                ('book_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment', models.IntegerField(default=0)),
                ('payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('refund_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('service', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='StationMaster.tbl_services')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
