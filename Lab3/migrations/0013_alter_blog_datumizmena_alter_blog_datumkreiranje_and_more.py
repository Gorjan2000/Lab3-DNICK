# Generated by Django 4.0.5 on 2022-06-02 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3', '0012_alter_blog_fajlovi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='datumIzmena',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='datumKreiranje',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='fajlovi',
            field=models.ImageField(blank=True, null=True, upload_to='cover_images/'),
        ),
    ]
