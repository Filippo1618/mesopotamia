# Generated by Django 4.2.1 on 2023-09-20 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("studio_agronomico", "0002_blogpost_followers"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="followed_blogposts",
            field=models.ManyToManyField(blank=True, to="studio_agronomico.blogpost"),
        ),
    ]