# Generated by Django 5.0.2 on 2024-03-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("slug", models.SlugField(unique=True)),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        db_index=True, max_length=150, verbose_name="Название статьи"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=150, unique=True, verbose_name="Слаг"
                    ),
                ),
                (
                    "body",
                    models.TextField(
                        blank=True, db_index=True, verbose_name="Содержимое статьи"
                    ),
                ),
                ("date_pub", models.DateTimeField(auto_now_add=True)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, related_name="posts", to="blog.tag"
                    ),
                ),
            ],
            options={
                "verbose_name": "Статья блога",
                "verbose_name_plural": "Статьи блога",
                "ordering": ["-date_pub"],
            },
        ),
    ]
