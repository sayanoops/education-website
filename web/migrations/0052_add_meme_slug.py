# Generated by Django 5.1.6 on 2025-04-01 16:15

from typing import Any

from django.db import migrations, models
from django.utils.text import slugify


def populate_meme_slugs(apps: Any, schema_editor: Any) -> None:
    Meme = apps.get_model("web", "Meme")
    for meme in Meme.objects.all():
        slug = slugify(meme.title)
        original_slug = slug
        counter = 1
        while Meme.objects.filter(slug=slug).exists():
            slug = f"{original_slug}-{counter}"
            counter += 1
        meme.slug = slug
        meme.save()


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0051_teamgoalmember_completion_image_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="meme",
            name="slug",
            field=models.SlugField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
        migrations.RunPython(populate_meme_slugs),
        migrations.AlterField(
            model_name="meme",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, unique=True),
        ),
    ]
