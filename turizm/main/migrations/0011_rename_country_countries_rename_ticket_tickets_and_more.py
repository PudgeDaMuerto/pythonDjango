# Generated by Django 4.0.4 on 2022-05-14 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_rename_countries_country_rename_tickets_ticket_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='Countries',
        ),
        migrations.RenameModel(
            old_name='Ticket',
            new_name='Tickets',
        ),
        migrations.RenameModel(
            old_name='User',
            new_name='Users',
        ),
    ]