# Generated by Django 4.0.5 on 2022-06-02 19:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Lab3', '0009_rename_komentar_komentari'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blokiran',
            name='bloker',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bloker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='blokiran',
            name='blokiran',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blokiran', to=settings.AUTH_USER_MODEL),
        ),
    ]
