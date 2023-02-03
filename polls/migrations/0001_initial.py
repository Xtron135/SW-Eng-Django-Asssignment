# Generated by Django 3.2.16 on 2023-02-02 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Soalan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_soalan', models.CharField(max_length=200)),
                ('tarikh_soalan', models.DateTimeField(verbose_name='data published')),
            ],
        ),
        migrations.CreateModel(
            name='Pilihan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teks_pilihan', models.CharField(max_length=200)),
                ('undi', models.IntegerField(default=0)),
                ('Soalan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.soalan')),
            ],
        ),
    ]
