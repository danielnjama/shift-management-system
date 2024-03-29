# Generated by Django 4.2.7 on 2024-03-08 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Backlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ReassignedTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SLAStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incident_id', models.CharField(max_length=100, verbose_name='Incident ID')),
                ('summary', models.TextField(verbose_name='Summary')),
                ('created_on', models.DateField(verbose_name='Created On')),
                ('resolved_on', models.DateField(blank=True, null=True, verbose_name='Resolved On')),
                ('dependency_reason', models.TextField(verbose_name='Dependency Reason')),
                ('engineer_responsible', models.CharField(max_length=100, verbose_name='Engineer responsible')),
                ('backlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.backlog', verbose_name='Backlog')),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.market', verbose_name='Market')),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.priority', verbose_name='Priority')),
                ('reassigned_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.reassignedteam', verbose_name='Reassigned Team')),
                ('sla_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.slastatus', verbose_name='SLA Status')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketmanagement.status', verbose_name='Status')),
            ],
        ),
    ]
