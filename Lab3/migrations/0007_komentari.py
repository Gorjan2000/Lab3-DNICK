# Generated by Django 4.0.5 on 2022-06-02 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lab3', '0006_alter_blog_avtor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Komentari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('komentar', models.TextField(max_length=400)),
                ('datumKreirano', models.DateTimeField(auto_now_add=True)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lab3.blog')),
                ('komentator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Lab3.bloguser')),
            ],
            options={
                'ordering': ['datumKreirano'],
            },
        ),
    ]