# Generated by Django 5.0.6 on 2024-05-15 12:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('profile', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.CharField(choices=[('new', 'Новая'), ('pending', 'В ожидании'), ('approved', 'Одобрена'), ('rejected', 'Отклонена'), ('closed', 'Закрыта')], default='new', max_length=20)),
                ('documents', models.FileField(blank=True, null=True, upload_to='documents/')),
                ('description', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('assigned_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deals_assigned', to='profile.profile')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deals_created', to='client.contact')),
            ],
        ),
    ]
