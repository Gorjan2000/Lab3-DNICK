# Generated by Django 4.0.5 on 2022-06-02 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3', '0002_alter_blog_avtor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogUser',
        ),
    ]