# Generated by Django 4.0.5 on 2022-06-02 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3', '0008_rename_komentari_komentar_blokiran'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Komentar',
            new_name='Komentari',
        ),
    ]
