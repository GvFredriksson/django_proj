# Generated by Django 2.2.6 on 2019-10-17 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField(blank=True)),
                ('imdb_score', models.IntegerField(blank=True)),
                ('hero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hero', to='super.Hero')),
                ('villain', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='villain', to='super.Hero')),
            ],
        ),
    ]