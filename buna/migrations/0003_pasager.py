# Generated by Django 3.1.5 on 2021-03-19 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buna', '0002_auto_20210317_1132'),
    ]

    operations = [
        migrations.CreateModel(
            name='pasager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=30)),
                ('prenume', models.CharField(max_length=30)),
                ('CAlatorie', models.ManyToManyField(blank=True, related_name='pasageri', to='buna.calatorie')),
            ],
        ),
    ]
