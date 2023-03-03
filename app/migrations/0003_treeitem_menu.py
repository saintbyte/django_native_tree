# Generated by Django 4.1.7 on 2023-03-02 17:48
import django.db.models.deletion
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_treeitem"),
    ]

    operations = [
        migrations.AddField(
            model_name="treeitem",
            name="menu",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.tree",
                verbose_name="Меню",
            ),
            preserve_default=False,
        ),
    ]
