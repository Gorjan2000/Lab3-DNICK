# Generated by Django 4.0.5 on 2022-06-02 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3', '0004_bloguser_alter_blog_avtor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='avtor',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Lab3.bloguser'),
            preserve_default=False,
        ),
    ]
